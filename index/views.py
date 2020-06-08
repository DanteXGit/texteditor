from django.shortcuts import render,redirect,get_object_or_404
from .models import ImageModel, PostModel, FileModel
from .forms import ImageForm, PostForm, FileForm
# Create your views here.
def index(request):
    posts = PostModel.objects.all()
    return render(request, "index/index.html", {'Posts':posts})

def editor(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        else:
            return render(request, 'index/editor.html', {'Form':form}) 
    else:
        form = PostForm()
        return render(request, 'index/editor.html', {'Form':form})

def post_detail(request, post_slug):
    post = get_object_or_404(PostModel,PostSlug=post_slug)
    gallery = ImageModel.objects.filter(Post=post)
    files = FileModel.objects.filter(Post=post)
    return render(request, 'index/post_detail.html',{'Post':post,'Images':gallery,'Files':files})

def post_edit(request, post_slug):
    post = get_object_or_404(PostModel,PostSlug=post_slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if(form.is_valid()):
            post = form.save()
            post.save()
            return redirect('post_detail',post_slug=post.PostSlug)
        else:
            return render(request, 'index/editor.html', {'Form':form}) 
    else:
        form = PostForm()
        return render(request, 'index/editor.html', {'Form':form})

def add_image(request, post_slug):
    if request.method == 'POST':
        # print(request.POST)
        form = ImageForm(request.POST, request.FILES)
        if(form.is_valid()):
            img = form.save(commit=False)
            form.save()
            return redirect('post_detail', post_slug=post_slug)
        form = ImageForm()
        return render(request, 'index/editor.html', {'Form':form})
    else:
        form = ImageForm()
        return render(request, 'index/editor.html', {'Form':form})

def add_file(request, post_slug):
    if request.method == 'POST':
        # print(request.POST)
        form = FileForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('post_detail', post_slug=post_slug)
        form = FileForm()
        return render(request, 'index/editor.html', {'Form':form})
    else:
        form = FileForm()
        return render(request, 'index/editor.html', {'Form':form})

def all_files(request):
    docs = FileModel.objects.all()
    return render(request, 'index/filter.html',{'Docs':docs})

def all_images(request):
    imgs = ImageModel.objects.all()
    return render(request, 'index/filter.html',{'Imgs':imgs})

def filtering(request):
    return render(request, 'index/filter.html')