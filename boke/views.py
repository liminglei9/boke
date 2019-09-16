from django.http import HttpResponse
from django.shortcuts import render
from bokeapp.models import *
def index(request):
    article=Article.objects.order_by('-date')[:6]
    recommend_article=Article.objects.filter(recommend=1)[:7]
    click_article=Article.objects.order_by('-click')[:12]
    return render(request,'index.html',locals())

def about(request):
    return render(request,'about.html')

def listpic(request):
    return render(request,'listpic.html')

def newslistpic(request,page=1):
    page=int(page)
    article=Article.objects.order_by('-date')
    paginator=Paginator(article,6)
    page_obj=paginator.page(page)
    current_page=page_obj.number
    start=current_page-3
    if start<1:
        start=0
    end=current_page+2
    if end>paginator.num_pages:
        end=paginator.num_pages
    if start == 0:
        end = 5
    if end==paginator.num_pages:
        start = paginator.num_pages - 5
    page_range=paginator.page_range[start:end]

    return render(request,'newslistpic.html',locals())

def base(request):
    return render(request,'base.html')
def articlecontext(request,id):
    id=int(id)
    article = Article.objects.get(id=id)
    click=article.click+1
    article.click=click
    article.save()
    return render(request,'articlecontext.html',locals())
def adddata(request):
    for i in range(100):
        article=Article()
        article.title='title_%s'%i
        article.context='context_%s'%i
        article.description='description_%s'%i
        article.author=Author.objects.get(id=3)
        article.save()
        article.type.add(Type.objects.get(id=3))
        article.save()
    return HttpResponse('增加数据')
from django.core.paginator import Paginator
def fytest(request):
    article=Article.objects.all().order_by("-date")
    paginator=Paginator(article,5)
    print(paginator.count)
    return HttpResponse('分页功能测试')