# Generated by Django 4.1.7 on 2023-05-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('Last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('Email', models.CharField(max_length=70, verbose_name='Почта')),
            ],
        ),
    ]
