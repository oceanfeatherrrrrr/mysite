# Generated by Django 2.2.12 on 2024-06-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=20, unique=True, verbose_name='user')),
                ('password', models.CharField(default='', max_length=64, verbose_name='pass')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='register_time')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
