from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates a default superuser if one does not exist.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'Feruzbek'
        email = 'feruzbek@gmail.com'
        password = '201120112011'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username_
