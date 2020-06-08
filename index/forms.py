from django.forms import ModelForm
from .models import PostModel,ImageModel,FileModel

class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ('Text','Title','PostSlug')

class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = ('File','Post',)

class FileForm(ModelForm):
    class Meta:
        model = FileModel
        fields = ('File','Post',)
