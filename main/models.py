from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField
    bio = models.TextField(blank=True, null=True)
    profileimg = models.ImageField(upload_to='profile_images', default='images.png')
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

