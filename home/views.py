from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.utils import timezone
from blog.models import Post
from accounts.forms import EmailRegisterForm

# Create your views here.


def get_index(request):
    if request.method == "POST":
        form = EmailRegisterForm(request.POST)
        form.save()
        messages.success(request, "You have been added to our mailing list")
        return redirect('home')
    else:
        form = EmailRegisterForm()
    
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')[0:4]
    return render(request, "home/index.html", {'posts': posts, 'form': form})
    
def get_about(request):
    return render(request, "home/about.html")
    
def get_contact(request):
    return render(request, "home/contact.html")