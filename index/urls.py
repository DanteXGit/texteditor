from django.urls import path,include
from .views import index,editor,post_detail,post_edit,add_image,add_file,all_images,all_files,filtering

urlpatterns = [
    path('', index, name='index'),
    path('editor', editor, name='add_post'),
    path('filter',filtering, name="filter_filess"),
    path('images', all_images, name='all_images'),
    path('files', all_files, name='all_files'),
    path('<slug:post_slug>', post_detail, name='post_detail'),
    path('<slug:post_slug>/edit', post_edit, name='post_edit'),
    path('<slug:post_slug>/addimage', add_image, name='add_image'),
    path('<slug:post_slug>/addfile', add_file, name='add_file'),
]
