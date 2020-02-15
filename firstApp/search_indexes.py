from haystack import indexes
from firstApp.models import c4d_url

class search_index_lab(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)
    def get_model(self):
        return  c4d_url
    def index_queryset(self, using=None):
        return self.get_model().objects.exclude(trans_title__isnull=True)
