from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
)


urlpatterns = [
    path('<int:post_id>/', blog_post_detail_view),
    path('', blog_post_list_view),
    path('<int:post_id>/edit', blog_post_update_view),
    path('<int:post_id>/delete', blog_post_delete_view),
]
