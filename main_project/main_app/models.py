from django.db import models
from django.db.models.fields import BooleanField, TextField

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.TextField(max_length=10)
    password = models.CharField(max_length=10)
    att_classes = models.IntegerField()
    total_classes = models.IntegerField()
    telugu_mid_marks = models.IntegerField()
    hindi_mid_marks = models.IntegerField()
    english_mid_marks = models.IntegerField()
    maths_mid_marks = models.IntegerField()
    science_mid_marks = models.IntegerField()
    social_mid_marks = models.IntegerField()
    telugu_final_marks = models.IntegerField()
    hindi_final_marks = models.IntegerField()
    english_final_marks = models.IntegerField()
    maths_final_marks = models.IntegerField()
    science_final_marks = models.IntegerField()
    social_final_marks = models.IntegerField()

    def __str__(self):
        return self.rollno
