from django.db import models

# Create your models here.


class PostModel(models.Model):
    Title = models.CharField(default='Заголвок', verbose_name='Заголовок статьи', max_length=100)
    Text = models.TextField(verbose_name='Текст')
    PostSlug = models.SlugField(default='Slug', verbose_name='Слаг файла',unique=True)
    def __str__(self):
        return self.Title
    class Meta:
        ordering =['-id']
    

class ImageModel(models.Model):
    File = models.ImageField(verbose_name='Изображение', upload_to='images/')
    Post = models.ForeignKey(verbose_name='Пост, к которому прикрепить',on_delete=models.CASCADE, to=PostModel)

class FileModel(models.Model):
    File = models.FileField(verbose_name='Файл', upload_to='files/')
    Post = models.ForeignKey(verbose_name='Пост, к которому прикрепить',on_delete=models.CASCADE, to=PostModel)
