from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author_post',
            'categories_post',
            'title_post',
            'text_post',
        ]