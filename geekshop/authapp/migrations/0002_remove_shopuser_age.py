# Generated by Django 2.1.7 on 2019-03-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='age',
        ),
    ]