from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


# for profile page
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # this is a one to one relation where one user can only have one profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"


# for create a signal where a user get a profile
@receiver(post_save, sender=User)
def Create_Profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()