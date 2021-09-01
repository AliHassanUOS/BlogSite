from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog_model(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    DateAndTime = models.DateTimeField(auto_now_add=True)
    