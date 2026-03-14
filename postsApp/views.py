from django.shortcuts import render, redirect, get_object_or_404
from .models import UserPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

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
    blog = get_object_or_404(UserPost, id=blog_id)
    
    return render(
        request,
        template_name='single_blog.html',
        context={'blog': blog}
    )
    
    
@login_required
def AddBlogView(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author = request.user
            blog.save()
            
        return redirect("home")
    
    else:
        form = BlogForm()
        return render(
            request,
            template_name="blogForm.html",
            context={
                "form": form
            }
        )
        
  
@login_required      
def deleteBlogView(request, blog_id):
    blog = get_object_or_404(UserPost, id=blog_id)
    blog.delete()
    return redirect("home")


def editBlogView(request, blog_id):
    blog = get_object_or_404(UserPost, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            
        return redirect("single-blog", blog.id)
        
    
    else:
        form = BlogForm(instance=blog)
        return render(
            request,
            template_name="blogForm.html",
            context={
                "form": form,
                "action": "Edit"
            }
        )
        