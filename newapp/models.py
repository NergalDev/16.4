from audioop import reverse

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

class Author(models.Model):

   
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

  
    ratingAuthor = models.SmallIntegerField(default=0)

    
    def update_rating(self):

       
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

       
        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        
        self.save()

   
    def __str__(self):
        return f'{self.authorUser}'



class Category(models.Model):

   
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('news_category', kwargs={'category_id': self.id})


class Post(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)

    dateCreation = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)

    title = models.CharField(max_length=128)

    text = models.TextField()

    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self): 
        return f'/news/{self.id}'


class Comment(models.Model):

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)

    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    dateCreation = models.DateTimeField(auto_now_add=True)

    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.commentUser}: {self.text[:20]}'
