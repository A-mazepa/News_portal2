from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.urls import reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_rating = models.FloatField(default=0.0)

    def update_rating(self):
        sum_rat_post = self.post_set.all().aggregate(Sum('rating_post'))['rating_post__sum']*3
        sum_rat_comments = self.user.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']
        sum_rat_comments_posts = self.post_set.all().aggregate(Sum('comment__rating_comment'))['comment__rating_comment__sum']
        self.rating_author = sum_rat_post + sum_rat_comments + sum_rat_comments_posts
        self.save()



class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name_category.title()


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    TYPE = [
    (article, 'статья'),
    (news, 'новость')]

    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=TYPE, default=article)
    date_time_post = models.DateTimeField(auto_now_add=True)
    categories_post = models.ManyToManyField(Category, through='PostCategory')
    title_post = models.CharField(max_length=250)
    text_post = models.TextField()
    rating_post = models.FloatField(default=0.0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[0:125]+'...'

    def __str__(self):
        return f'{self.title_post.title()}: {self.text_post[:25]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    data_time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()

    def __str__(self):
        return self.text_comment[:20]