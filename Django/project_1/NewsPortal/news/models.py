
from django.db import models
from django.contrib.auth.models import User


news = 'NE'
article = 'AR'

CHOICES =( 
        (news, "Новость"), 
        (article, "Статья"), 
    ) 



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)

    

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
                    
# суммарный рейтинг каждой статьи автора умножается на 3; 15
# суммарный рейтинг всех комментариев автора; 19
# суммарный рейтинг всех комментариев к статьям автора. 22

class Category(models.Model):
    category = models.CharField(max_length = 24, unique = True)

class Post(models.Model):


    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    choise = models.CharField(max_length = 2, choices=CHOICES, default = news)
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


# связь «один ко многим» с моделью Post;
# связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
# текст комментария;
# дата и время создания комментария;
# рейтинг комментария.

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
# основываясь на лайках/дислайках к этой статье.
        
# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.