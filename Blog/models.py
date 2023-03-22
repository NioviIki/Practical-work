from django.db import models
from django.contrib.auth.models import User
import datetime
class Posts(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date.date()}, {self.date.time()}'
