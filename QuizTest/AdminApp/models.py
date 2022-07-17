from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100,default="The language for building web pages")

    def __str__(self):
        return self.cat_name

    class Meta:
        db_table = "Category"

class Question(models.Model):
    que = models.CharField(max_length=1000)
    ans = models.CharField(max_length=20)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)

    class Meta:
        db_table = "Question"