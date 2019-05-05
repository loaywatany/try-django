from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BLogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        instance = self.instance
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():    
            raise forms.ValidationError("This title has already been used, Please enter something new")
        return title 
