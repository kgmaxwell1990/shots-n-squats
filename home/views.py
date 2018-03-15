from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def get_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')[0:4]
    return render(request, "home/index.html", {'posts': posts})
    
def get_about(request):
    return render(request, "home/about.html")
    
def get_contact(request):
    return render(request, "home/contact.html")