from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
GENDER_LIST=(
    (1,'男'),
    (2,'女'),
)
class Author(models.Model):
    name=models.CharField(max_length=32,verbose_name='名字')
    age=models.IntegerField(verbose_name='年龄')
    # gender=models.CharField(max_length=8,verbose_name='性别')
    gender=models.IntegerField(choices=GENDER_LIST,verbose_name='性别',default=1)
    email=models.CharField(max_length=32,verbose_name='邮箱')
    def __str__(self):
        return self.name
    class Meta:
        db_table='author'
        verbose_name='作者'
        verbose_name_plural=verbose_name
class Type(models.Model):
    name=models.CharField(max_length=32,verbose_name='类型')
    description=models.TextField(verbose_name='描述')
    def __str__(self):
        return self.name
    class Meta:
        db_table='type'
        verbose_name='类型'
        verbose_name_plural=verbose_name
class Article(models.Model):
    title=models.CharField(max_length=32,verbose_name='标题')
    date=models.DateField(auto_now=True,verbose_name='日期')
    # context=models.TextField(verbose_name='文章')
    context=RichTextField(verbose_name='文章')
    # description=models.TextField(verbose_name='描述')
    description=RichTextField(verbose_name='描述')
    recommend=models.IntegerField(verbose_name='推荐',default=0)
    click=models.IntegerField(verbose_name='点击率',default=0)
    picture=models.ImageField(upload_to='images',default='images/01.jpg')
    author=models.ForeignKey(to=Author,on_delete=models.SET_DEFAULT,default=1)
    type=models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
        db_table='article'
        verbose_name='文章'
        verbose_name_plural=verbose_name
