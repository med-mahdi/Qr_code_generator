# Generated by Django 4.1.4 on 2023-07-21 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationApp', '0006_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='hoobie',
        ),
        migrations.DeleteModel(
            name='Hobbies',
        ),
    ]
