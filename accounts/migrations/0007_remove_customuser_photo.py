# Generated by Django 5.0.3 on 2024-03-26 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_customuser_img_customuser_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='photo',
        ),
    ]