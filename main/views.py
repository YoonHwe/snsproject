from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json

# Create your views here.
def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def show_show(request):
    return render(request, 'main/show.html')

def show_past(request):
    return render(request, 'main/past.html')

def show_present(request):
    return render(request, 'main/present.html')

def show_future(request):
    return render(request, 'main/future.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html',{'post':post, 'comments': all_comments})

def new(request):
    return render(request, 'main/new.html')

def more(request):
    posts = Post.objects.all()
    return render(request, 'main/more.html', {'posts':posts})

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now() 
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post': edit_post})

def update(request, id):
    update_post = get_object_or_404(Post, id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now() 
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:more')

def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk = post_id)
    new_comment.save()
    return redirect('main:detail', post_id)

def edit_comment(request, post_id):
    edit_comment = Comment.objects.get(id = post_id)
    return render(request, 'main/edit_comment.html', {'comment': edit_comment})

def update_comment(request, post_id):
    update_comment = get_object_or_404(Comment, id = post_id)
    update_comment.writer = request.user
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('main:detail', update_comment.post_id)

def delete_comment(request, post_id):
    delete_comment = Comment.objects.get(id=post_id)
    delete_comment.delete()
    return redirect('main:more')

@login_required
@require_POST

def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    
    context = {
        "like_count":post.like_count,
        "result":result
    }

    return HttpResponse(json.dumps(context), content_type="application/json")

def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    
    context = {
        "dislike_count":post.dislike_count,
        "result":result
    }

    return HttpResponse(json.dumps(context), content_type="application/json")