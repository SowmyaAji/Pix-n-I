from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import DeleteView
from database.models import Post, Like
from django.http import HttpResponseRedirect
from database.forms import UpdatePostForm


class HomePage(View):
    def get(self, request):
        context = {}
        # code to query the database goes here!
        posts = Post.objects.all()[::-1]
        # add data to context
        context["posts"] = posts
        return render(request, 'index.html', context)


class PostPage(View):
    def get(self, request, postID):
        context = {}
        post = Post.objects.get(id=postID)
        context["post"] = post
        return render(request, 'post.html', context)


class CreatePost(View):
    def post(self, request):
        name = request.POST.get("name")
        url = request.POST.get("imgURL")
        caption = request.POST.get("caption")
        post = Post(imgURL=url, caption=caption, postedBy=name)
        post.save()
        return HttpResponseRedirect("/")


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect("/")


def edit_post(request, pk):

    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdatePostForm(
            data=request.POST, files=request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/', pk=post.pk)

    else:
        form = UpdatePostForm(instance=post)

    return render(request, 'edit_post.html', {
        'post': post,
        'form': form,
    })
