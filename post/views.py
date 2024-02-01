import math
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request, page_number=1):
    article_list = Article.objects.all().order_by('-created')
    # 创建分页器对象
    page_obj = Paginator(article_list, per_page=10)
    # 获取当前页的数据
    # page_number = request.GET.get('page_number', 1) # unicode字符串

    first_page_number = 1
    last_page_number = page_obj.num_pages

    page_number = int(page_number)
    per_page_list = page_obj.page(page_number)

    begin = (page_number - int(math.ceil(10.0 / 2)))
    # 每一页开始页面
    if begin < 1:
        begin = 1

    # 每一页结束页码
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    page_range = range(begin, end + 1)

    return render(request, 'index.html', {'article_list': per_page_list,
                                          'page_range': page_range,
                                          'page_number': page_number,
                                          'first_page_number': first_page_number,
                                          'last_page_number': last_page_number,
                                          })


def get_previous_article(current_article_id):
    try:
        previous_article = Article.objects.filter(id__lt=current_article_id).order_by('-id').first()
        if previous_article:
            return previous_article
        else:
            return None  # 没有找到前一个 article_id
    except Article.DoesNotExist:
        return None  # 处理异常情况


def get_next_article(current_article_id):
    try:
        next_article = Article.objects.filter(id__gt=current_article_id).order_by('-id').first()
        if next_article:
            return next_article
        else:
            return None  # 没有找到前一个 article_id
    except Article.DoesNotExist:
        return None  # 处理异常情况


def read(request, article_id):
    article_id = int(article_id)
    article_detail = Article.objects.get(id=article_id)

    previous_article = get_previous_article(article_id)
    next_article = get_next_article(article_id)
    # recommend_articles = Article.objects.filter(category=article_detail.category).order_by('-created')[:5]  # 可以优化
    recommend_articles = Article.objects.filter(category=article_detail.category).order_by('-created').values('id', 'title')[:5]
    return render(request, 'detail.html', {'article_detail': article_detail,
                                           'previous_article': previous_article,
                                           'next_article': next_article,
                                           'recommend_articles': recommend_articles})


'''需要优化'''


def category(request, cid):
    page_number = 1
    article_list = Article.objects.filter(category=cid).order_by('-created')
    # 创建分页器对象
    page_obj = Paginator(article_list, per_page=10)

    first_page_number = 1
    last_page_number = page_obj.num_pages

    page_number = int(page_number)
    per_page_list = page_obj.page(page_number)

    begin = (page_number - int(math.ceil(10.0 / 2)))
    # 每一页开始页面
    if begin < 1:
        begin = 1

    # 每一页结束页码
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    page_range = range(begin, end + 1)

    return render(request, 'index.html', {'article_list': per_page_list,
                                          'page_range': page_range,
                                          'page_number': page_number,
                                          'first_page_number': first_page_number,
                                          'last_page_number': last_page_number,
                                          })


def archive(request, year, month):
    page_number = 1
    article_list = Article.objects.filter(created__year=year, created__month=month).order_by('-created')
    # 创建分页器对象
    page_obj = Paginator(article_list, per_page=10)

    first_page_number = 1
    last_page_number = page_obj.num_pages

    page_number = int(page_number)
    per_page_list = page_obj.page(page_number)

    begin = (page_number - int(math.ceil(10.0 / 2)))
    # 每一页开始页面
    if begin < 1:
        begin = 1

    # 每一页结束页码
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    page_range = range(begin, end + 1)

    return render(request, 'index.html', {'article_list': per_page_list,
                                          'page_range': page_range,
                                          'page_number': page_number,
                                          'first_page_number': first_page_number,
                                          'last_page_number': last_page_number,
                                          })
