from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='body', null=True)
    num_likes = indexes.IntegerField(model_attr='num_likes')

    def get_model(self):
        return Post

