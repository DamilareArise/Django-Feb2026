from django.shortcuts import render
from .models import UserPost

# Create your views here.

def homeView(request):
    # blogs = UserPost.objects.all()
    # blogs = UserPost.objects.filter(status="PUBLISHED")
    # blogs = UserPost.objects.all().order_by("-updated_at")
    # blogs = UserPost.objects.filter(author=request.user)
    blogs = UserPost.objects.filter(status="PUBLISHED")[:3]
    
    return render(
        request,
        template_name="index.html",
        context={"blogs": blogs}
    )
    

def aboutView(request):
    
    return render(
        request,
        template_name="about.html",
        context={}
    )
    
    
def allBlogsView(request):
    blogs = UserPost.objects.filter(status="PUBLISHED")
    
    return render(
        request,
        template_name="blogs.html",
        context={'blogs': blogs}
    )
    
    
def singleBlogView(request, blog_id):
    blog = UserPost.objects.get(id = blog_id)
    
    return render(
        request,
        template_name='single_blog.html',
        context={'blog': blog}
    )