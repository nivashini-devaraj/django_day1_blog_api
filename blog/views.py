from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import BlogSerializer   
from django.shortcuts import render
from .models import Blog
from django.shortcuts import redirect, get_object_or_404


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()         
    serializer_class = BlogSerializer 

def blog_create(request):
    if request.method == 'POST':
        Blog.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user   
        )
        return redirect('blog-list-page')

    return render(request, 'blog/blog_create.html')


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_edit(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog-list-page')

    return render(request, 'blog/blog_edit.html', {'blog': blog})


def blog_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('blog-list-page')