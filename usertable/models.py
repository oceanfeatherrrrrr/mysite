from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('user', max_length=20, default='', unique=True)
    password = models.CharField('pass', max_length=256, default='')
    reg_date = models.DateTimeField('register_time', auto_now_add=True)
    class Meta:
        db_table = 'user'

