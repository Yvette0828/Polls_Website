from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

# Create your models here.

# Create two models: Question and Choice
# Each model has a number of class variables, each of which represents a database field in the model.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    # admin site display configration
    @admin.display(
            boolean = True,
            ordering = 'pub_date',
            description = 'Published recently?',
            )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    @property
    def total_votes(self):
        return self.choice_set.aggregate(total=models.Sum('votes'))['total'] or 0

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class PollOption(models.Model):
    name = models.CharField(max_length=200)