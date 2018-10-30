from django.db.models.signals import post_save;
from django.contrib.auth.models import User;
from users.models import Profile;
from django.dispatch import receiver;
@receiver(post_save,sender=User)
def create_prpfile(sender,created,instance,**kwargs):
    if created:
        Profile.objects.create(user=instance).save();
