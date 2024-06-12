from django.db import models

# Create your models here.

class QNA(models.Model):
    part = models.CharField('part', max_length=10)
    question = models.TextField('question')
    answer = models.TextField('answer')
    add_date = models.DateTimeField('add_time', auto_now_add=True)
    ch_date = models.DateTimeField('ch_time', auto_now_add=True)
    class Meta:
        db_table = 'question_and_answer'