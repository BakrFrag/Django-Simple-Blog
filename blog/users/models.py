from django.db import models

# Create your models here.
from django.contrib.auth.models import User;
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile");
    image=models.ImageField(upload_to="users_pictures",default="default.jpg");
    def __str__(self):
        return f'{self.user.username} profile';
