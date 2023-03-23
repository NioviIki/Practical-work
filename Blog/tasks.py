from celery import shared_task
from django.core.mail import send_mail
from core import settings
from .models import Comments, Posts
from django.contrib.auth.models import User

@shared_task()
def send_massage(recipient_list, message,
                 from_email=settings.EMAIL_HOST_USER):

    return send_mail(subject=f'new message',
                     message=message,
                     from_email=from_email,
                     recipient_list=[recipient_list],
                     auth_password=settings.EMAIL_HOST_PASSWORD)

@shared_task(serializer='json')
def add_to_comment(author, comment, pk, link):
    Comments.objects.create(author=author, comment=comment, post=Posts.objects.get(pk=pk))
    send_massage.apply_async(args=[settings.EMAIL_HOST_USER, f'new message'])
    send_massage.apply_async(args=[Posts.objects.get(pk=pk).owner.email, link])
    return f'Comment created by "{author}", comment: {comment}'

@shared_task()
def add_to_post(name, text, subject):
    Posts.objects.create(owner=User.objects.get(username=name), text=text, subject=subject)
    send_massage.apply_async(args=[settings.EMAIL_HOST_USER])
    return f'Post created by {name}, text: {subject}'

