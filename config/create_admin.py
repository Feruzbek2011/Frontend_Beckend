# config/create_admin.py
import os
import django

# Django'ni ishga tushirish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'Feruzbek'
email = 'feruzbek@gmail.com'
password = '201120112011'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superuser created successfully.")
else:
    print("ℹ️  Superuser already exists.")
