from celery import shared_task
from django.core.mail import send_mail
from core import settings


@shared_task()
def send_massage(recipient_list, message,
                 from_email=settings.EMAIL_HOST_USER):

    return send_mail(subject=f'new message',
                     message=message,
                     from_email=from_email,
                     recipient_list=[recipient_list],
                     auth_password=settings.EMAIL_HOST_PASSWORD)
