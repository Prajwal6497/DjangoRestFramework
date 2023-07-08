from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=30)
    esal = models.IntegerField()

    def __str__(self):
        return self.ename