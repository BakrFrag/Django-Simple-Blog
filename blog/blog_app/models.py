from django.db import models
from django.contrib.auth.models import User;
from django.utils import timezone;
from django.urls import reverse;
# Create your models here.
#django.urls import reverse => args kwargs
#django.shortcuts import redirect => name
class Post(models.Model):
    title=models.CharField(max_length=100);
    content=models.TextField();
    date=models.DateTimeField(default=timezone.now);
    author=models.ForeignKey(User,on_delete=models.CASCADE);
    def __str__(self):
        return self.title;
    class meta:
        verbose_name_plural="Blog Posts";
    #get_absolute_url
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.id});
