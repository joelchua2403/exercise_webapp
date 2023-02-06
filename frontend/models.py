from django.db import models
import csv

# Create your models here.
class Exercise(models.Model):
    id = models.IntegerField(primary_key=True)
    muscle_group = models.CharField(max_length=100)
    exercise = models.TextField(max_length=100)
    level = models.TextField(max_length=100)
    u_l_c = models.TextField(max_length=100)
    p_p = models.TextField(max_length=100)
    modality = models.TextField(max_length=100)
    joint = models.TextField(max_length=100)

    def __str__(self):
        return self.id, self.exercise



