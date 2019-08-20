import datetime

from django.db import models
from django.utils import timezone

class Product(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    question_text = 'Senior'
    pub_date = datetime.datetime.now()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     # question = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # choice_text = models.CharField(max_length=200)
#     # votes = models.IntegerField(default=0)
#     choice_text = 'test'
#     def __str__(self):
#         return self.choice_text