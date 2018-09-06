import random
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ActivationCode(models.Model):
    activation_code = models.CharField(max_length=10, primary_key=True)
    credentials = models.OneToOneField('Credentials', on_delete=models.CASCADE)


class Credentials(models.Model):

    class Meta:
        verbose_name_plural = 'Credentials'

    cea_login = models.CharField(max_length=30)
    cea_password = models.CharField(max_length=30)

    cima_login = models.CharField(max_length=30)
    cima_password = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        letters = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ'
        digits = '23456789'
        code = ''.join([random.choice(letters + digits) for _ in range(10)])
        ActivationCode.objects.create(activation_code=code, credentials=self)
