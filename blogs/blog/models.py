from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    author = models.CharField(max_length=50)
    imgpath = models.CharField(max_length=100)
    pro_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile = models.BigIntegerField()