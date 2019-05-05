from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPostManager(models.Manager):
    def published(self):
        now = timezone.now()
        return self.get_queryset().filter(publish_date__lte=now)

class BlogPost(models.Model):
    user         = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image        = models.FileField(upload_to='image', blank=True, null=True)
    title        = models.CharField(max_length=120)
    slug         = models.SlugField(unique=True)
    content      = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = BlogPostManager()
    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.id}"

    def get_edit_url(self):
        return f"/blog/{self.id}/edit" 

    def get_delete_url(self):
        return f"/blog/{self.id}/delete"            
        
    