"""pixnme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from pixnme.views import HomePage, PostPage, CreatePost, post_remove, edit_post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('<postID>', PostPage.as_view()),
    path('createPost/', CreatePost.as_view(), name="createPost"),
    path('post/<pk>/remove/', post_remove, name='post_remove'),
    # path('post/<pk>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/edit/', edit_post, name='edit_post'),
]
