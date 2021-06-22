from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

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
<<<<<<< HEAD
    return render(request, 'main/detail.html', {'post':post})
=======
    return render(request, 'main/detail.html',{'post':post})
>>>>>>> 021553fc165883fe174d18e03eea355a32959e76

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer'] 
    new_post.pub_date = timezone.now() 
    new_post.body = request.POST['body']
    new_post.image = request.FILES['image']
    new_post.save()
<<<<<<< HEAD
    return redirect('detail', new_post.id)
=======
    return redirect('main:detail', new_post.id)
>>>>>>> 021553fc165883fe174d18e03eea355a32959e76

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post': edit_post})

def update(request, id):
<<<<<<< HEAD
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)
=======
    update_post = Post()
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer'] 
    update_post.pub_date = timezone.now() 
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:showmain')
>>>>>>> 021553fc165883fe174d18e03eea355a32959e76
