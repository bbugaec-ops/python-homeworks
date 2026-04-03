from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, LoginForm, RegisterForm
from .models import Post, Category, Tag, Comment, Profile


def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    first_half = all[:half]
    second_half = all[half:]
    return {'cat_left': first_half, 'cat_right': second_half}


def get_tags():
    return {'all_tags': Tag.objects.all()}


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/index.html", context)


def contacts(request):
    context = {}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/contact.html", context)


def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        text = request.POST.get('text')
        if author_name and text:
            Comment.objects.create(post=post, author_name=author_name, text=text)
            return redirect('post_detail', slug=post.slug)

    context = {'post': post, 'comments': comments}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/post.html", context)


def category(request, slug=None):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/index.html", context)

def tag_posts(request, slug=None):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag).order_by("-published_date")
    context = {'posts': posts, 'current_tag': tag}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/index.html", context)

def search(request):
    query = request.GET.get('qwery')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))

    context = {'posts': posts}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/index.html", context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            form.save_m2m()
            return redirect('post_detail', slug=new_post.slug)
    form = PostForm()
    context = {'form': form}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, 'blog/create.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Невірний логін або пароль')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'registracion/login.html', context)


def user_logout(request):
    logout(request)
    return render(request, 'registracion/logged_out.html')


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    return render(request, "blog/profile.html")