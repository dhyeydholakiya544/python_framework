from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    age = models.IntegerField()


class Author(models.Model):
    aname = models.CharField(max_length=20)

   
    

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    bname = models.CharField(max_length=30)
    price = models.IntegerField()
