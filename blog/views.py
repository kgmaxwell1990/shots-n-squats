from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseForbidden
from .models import Post
from .forms import BlogPostForm

# Create your views here.
def get_blog(request):
    blog_posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blog/blog.html", {'blog_posts': blog_posts})
    
def view_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    can_edit = post.can_be_edited_by(request.user)
    return render(request, "blog/view_post.html", {'post': post, 'can_edit': can_edit})

def new_post(request):
    
    if not request.user.is_staff:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(view_post, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/new_post.html', {'form': form})
    
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
   
    if not post.can_be_edited_by(request.user):
       return HttpResponseForbidden()
   
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(view_post, post.pk)
    else:
       form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})