from haystack import indexes
from post.models import *


# 注意class名称（"模型类名+Index"）
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)  # 固定的

    # 给title和content设置索引
    title = indexes.NgramField(model_attr='title') # model_attr指定对应的模型字段
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')