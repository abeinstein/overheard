from django.shortcuts import render
from vanilla import ListView

from .models import Post

class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        return Post.objects.order_by('-num_likes').exclude(body__isnull=True).exclude(body__exact='')