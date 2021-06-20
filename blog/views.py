from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    search=request.GET.get('search')
    if search =="true":
        author=request.GET.get('name')
        blogs=Blog.objects.filter(writer=author)
        return render(request,"home.html",{"blogs":blogs})
    paginator=Paginator(blogs,2)
    page=request.GET.get('page')  #몇번째 페이지인지 정보받음
    blogs=paginator.get_page(page)  #그 페이지에 해당하는 글들 가져옴
    return render(request,"home.html",{"blogs":blogs})

def detail(request,id):
    blog=get_object_or_404(Blog,pk=id)
    return render(request, "detail.html",{'blog':blog})

def new(request):
    form=BlogForm
    return render(request, "new.html",{'form':form})

def create(request):
    form=BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.pub_date=timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect("home")

def edit(request,id):
    edit_blog=Blog.objects.get(id=id)
    return render(request,"edit.html",{"blog":edit_blog})

def update(request,id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect("detail",update_blog.id)

def delete(request,id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect("home")


