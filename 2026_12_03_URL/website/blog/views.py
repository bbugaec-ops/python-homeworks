from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag, Comment


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


def tag(request, slug=None):
    t = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=t).order_by("-published_date")
    context = {'posts': posts, 'current_tag': t}
    context.update(get_categories())
    context.update(get_tags())
    return render(request, "blog/index.html", context)
