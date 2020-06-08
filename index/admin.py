from django.contrib import admin
from .models import ImageModel,PostModel,FileModel
# Register your models here.
admin.site.register(ImageModel)
admin.site.register(PostModel)
admin.site.register(FileModel)
