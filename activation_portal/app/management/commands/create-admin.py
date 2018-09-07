from django.contrib.auth.management.commands import createsuperuser
from django.contrib.auth.models import User


class Command(createsuperuser.Command):

    def handle(self, *args, **kwargs):
        username = 'admin'
        password = 'admin'
        if not User.objects.filter(username=username).exists():
            user = User(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
