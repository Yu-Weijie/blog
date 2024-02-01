from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    cname = models.CharField(verbose_name='类别名称', max_length=32, unique=True)

    def __str__(self):
        return self.cname


class Tag(models.Model):
    tname = models.CharField(verbose_name='标签名称', max_length=32, unique=True)

    def __str__(self):
        return self.tname

class Article(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=32, unique=True)
    describe = models.CharField(verbose_name="文章描述", max_length=128)
    # content = models.TextField(verbose_name="文章内容")
    content = RichTextUploadingField(verbose_name='文章内容', null=True, blank=True, config_name='default')
    # content = RichTextField(verbose_name='文章内容', null=True, blank=True)
    created = models.DateTimeField(verbose_name="发帖时间", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
