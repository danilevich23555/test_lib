from django.core.mail import EmailMessage, EmailMultiAlternatives
from celery import shared_task

from Library.settings import EMAIL_HOST_USER
from backend.models import User


@shared_task()
def send_mail(subject, message, email):
    msg = EmailMessage(subject, message, from_email=EMAIL_HOST_USER, to=[email])
    msg.send()
