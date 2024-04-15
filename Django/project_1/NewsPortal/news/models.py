
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _




class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.user.username
    

    def uppdate_rating(self):

        if Post.objects.filter(author=self).exists():
            __posts_rating = Post.objects.filter(author=self).values('rating')
            self.rating += sum(item['rating'] for item in __posts_rating)*3
            self.save()
        
        if Comment.objects.filter(user=self.user).exists():
            __comments_rating = Comment.objects.filter(user=self.user).values('rating')
            self.rating += sum(item['rating'] for item in __comments_rating)
            self.save()

        if Comment.objects.filter(post__author=self).exists():
            __postComments_rating = Comment.objects.filter(post__author=self).values('rating')
            self.rating += sum(item['rating'] for item in __postComments_rating)
            self.save()
                    

class Category(models.Model):
    category = models.CharField(max_length = 24, unique = True)

    def __str__(self) -> str:
        return self.category

class Post(models.Model):

    class PostType(models.TextChoices):

        news = 'NE', _('Новость')
        article = 'AR', _('Статья')


    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    choise = models.CharField(max_length = 2, choices=PostType, default = PostType.news)
    creation_date = models.DateTimeField(auto_now_add = True)
    post_header = models.CharField(max_length=64)
    post_text = models.TextField(default='Some text', max_length=512)
    rating = models.IntegerField(default=0)

    category = models.ManyToManyField(Category, through = 'PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.post_text) > 124:
            return f"{str(self.post_text)[:124]}..."
        else:
            return f"{str(self.post_text)}"

    def __str__(self):
        return f'Название: {self.post_header}, Автор: {self.author.user.username}, Рейтинг: {self.rating}'
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=64)
    creation_date = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

