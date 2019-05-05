from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
from .forms import BLogPostModelForm
from .models import BlogPost


def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    template_name = 'list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


#@login_required(login_url='/login')
@staff_member_required
def blog_post_create_view(request):
    form = BLogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BLogPostModelForm()
    template_name = 'form.html'
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = 'detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    form = BLogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"form": form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)