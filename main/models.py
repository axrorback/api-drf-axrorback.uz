from django.db import models
import uuid
import os
from django.contrib.auth.models import AbstractUser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def upload_hero_image(filename):
    return os.path.join(BASE_DIR/'media'/'hero_images', filename)
def upload_achievement(filename):
    return os.path.join(BASE_DIR/'media'/'achievements', filename)




class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username



class Achievements(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_achievement)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class  About(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    social_account_name = models.CharField(max_length=50)
    social_account_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_hero_image)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title



class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    question = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=100 , blank=True , null=True)
    answered_at = models.DateTimeField(blank=True , null=True)
    answered_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE , blank=True , null=True)

    def __str__(self):
        return self.question

