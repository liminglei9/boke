# Generated by Django 2.2.1 on 2019-09-16 13:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokeapp', '0003_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click',
            field=models.IntegerField(default=0, verbose_name='点击率'),
        ),
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0, verbose_name='推荐'),
        ),
        migrations.AlterField(
            model_name='article',
            name='context',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]