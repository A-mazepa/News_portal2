from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
from .forms import PostForm
from .filters import PostFilter

class PostsList(ListView):
    model = Post
    ordering = 'title_post'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(CreateView):

    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'