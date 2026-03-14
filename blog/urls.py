"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from postsApp.views import homeView, aboutView, allBlogsView, singleBlogView, AddBlogView, deleteBlogView,  editBlogView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path("about/", aboutView, name="about"),
    path('blogs/', allBlogsView, name='blogs'),
    path('single-blog/<int:blog_id>/', singleBlogView, name='single-blog'),
    path('add-blog/', AddBlogView, name='add-blog'),
    path('delete-blog/<int:blog_id>/', deleteBlogView, name="delete-blog"),
    path('edit-blog/<int:blog_id>/', editBlogView, name="edit-blog")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)