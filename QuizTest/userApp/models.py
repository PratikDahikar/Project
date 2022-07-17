# from unicodedata import category
from django.db import models
from AdminApp.models import Category

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "UserInfo"

class allResult(models.Model):
    user = models.ForeignKey(UserInfo,on_delete= models.CASCADE)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    correct = models.CharField(max_length=2)
    total = models.CharField(max_length=2)
    per = models.CharField(max_length=3)

    class Meta:
        db_table = "AllResult"

