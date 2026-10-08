from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=30, null=False)
    author = models.CharField(max_length=30, null=False)
    editorial = models.CharField(max_length=30)

    def info(self):
        return f"The {self.title} book was written by {self.author}"
        

class user(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=10)