from django.shortcuts import render
from .models import *
# Create your views here.

def error_404(request):
    return render(request,'404.html')
def error_500(request):
    return render(request,'404.html')


def index(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio.html')
def blog(request):
    blogs = Blogs.objects.all().order_by('-id')
    return render(request,'blog.html',{"blogs":blogs})
def gallery(request):
    img = Post.objects.all().order_by('-id')
    return render(request,'gallery.html',{"img":img})
def projects(request):
    pro = Projects.objects.all().order_by('-id')
    return render(request,'projects.html',{"pro":pro})
def services(request):
    return render(request,'services.html')

def chatme(request):
    return render(request,'chatme.html')
def contact(request):
    return render(request,'contact.html')
def loading(request):
    return render(request,'loading.html')