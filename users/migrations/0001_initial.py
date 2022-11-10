# Generated by Django 4.1.3 on 2022-11-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Местоположение')),
                ('lat', models.DecimalField(decimal_places=10, max_digits=15, null=True, verbose_name='Широта')),
                ('lng', models.DecimalField(decimal_places=10, max_digits=15, null=True, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Никнейм')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('role', models.CharField(choices=[('member', 'Пользователь'), ('admin', 'Администратор'), ('moderator', 'Модератор')], default='member', max_length=16, verbose_name='Группа')),
                ('age', models.PositiveIntegerField(null=True, verbose_name='Возраст')),
                ('location', models.ManyToManyField(to='users.location', verbose_name='Местоположение')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]