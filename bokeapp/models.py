from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=32,verbose_name='名字')
    age=models.IntegerField(verbose_name='年龄')
    gender=models.CharField(max_length=8,verbose_name='性别')
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
    context=models.TextField(verbose_name='文章')
    description=models.TextField(verbose_name='描述')
    author=models.ForeignKey(to=Author,on_delete=models.SET_DEFAULT,default=1)
    type=models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
        db_table='article'
        verbose_name='文章'
        verbose_name_plural=verbose_name
