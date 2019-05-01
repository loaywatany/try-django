from django.http import Http404
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import BlogPostForm
from .models import BlogPost


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    template_name = 'form.html'
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = 'detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = 'update.html'
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = 'delete.html'
    context = {"object": obj}
    return render(request, template_name, context)