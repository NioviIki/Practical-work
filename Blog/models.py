from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    subject = models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date.date()}, {self.date.time()}'
