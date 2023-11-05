from django.db import models
import datetime
# Create your models here.
class Task(models.Model):
    def __int__(self):
        return self.date
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)
