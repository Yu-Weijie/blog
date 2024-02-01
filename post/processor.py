from django.db.models.functions import TruncMonth
from django.db.models import Count
from .models import Article


def get_right(request):
    right_category = Article.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')
    right_latest = Article.objects.all().order_by('-created')[:10]
    right_date = Article.objects.annotate(month=TruncMonth('created')).values('month').annotate(
        count=Count('id')).order_by('month')
    article_counts = Article.objects.count()
    return {
        'right_category': right_category,
        'right_latest': right_latest,
        'right_date': right_date,
        'article_counts': article_counts,
    }
