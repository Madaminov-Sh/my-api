from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.date}"
