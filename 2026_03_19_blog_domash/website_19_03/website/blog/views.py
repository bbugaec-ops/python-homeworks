from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now

from .models import Post, Category, Comment, Subscriber
from .forms import PostForm, LoginForm, CommentForm, SubscribeForm, RegisterForm


def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    first_half = all[:half]
    second_half = all[half:]
    return {'cat_left': first_half, 'cat_right': second_half}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    subscribe_form = SubscribeForm()
    context = {'posts': posts}
    context.update(get_categories())
    context['subscribe_form'] = subscribe_form
    return render(request, "blog/index.html", context)


def contacts(request):
    context = {'subscribe_form': SubscribeForm()}
    context.update(get_categories())
    return render(request, "blog/contact.html", context)


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(
                post=post,
                author_name=comment_form.cleaned_data['author_name'],
                text=comment_form.cleaned_data['text']
            )
            return redirect('post_detail', slug=post.slug)

    context = {'post': post, 'comments': comments, 'comment_form': comment_form, 'subscribe_form': SubscribeForm()}
    context.update(get_categories())
    return render(request, "blog/post.html", context)


def category(request, slug=None):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {'posts': posts, 'subscribe_form': SubscribeForm()}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    context = {'posts': posts, 'subscribe_form': SubscribeForm()}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = now()
            new_post.user = request.user
            new_post.save()
            form.save_m2m()  # тільки для manytomany звязків
            return index(request)
    form = PostForm()
    context = {'form': form}
    return render(request, 'blog/create.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {'form': form, 'subscribe_form': SubscribeForm()}
    context.update(get_categories())
    return render(request, 'registration/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Невірний логін або пароль')

    form = LoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def subscribe_news(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            Subscriber.objects.get_or_create(email=form.cleaned_data['email'])
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {'post': post}
    context.update(get_categories())
    return render(request, "blog/delete_confirm.html", context)
