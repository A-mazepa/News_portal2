from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {

            'title_post': ['icontains'],
            'author_post': ['icontains'],
            'date_time_post': [

                'gt',
            ],
        }