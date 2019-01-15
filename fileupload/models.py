from django.db import models
from fileupload.test_choices import *
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    class Meta:
        abstract = True


class test_files(UserData):
    Name = models.CharField(max_length=50)
    Jahrgang = models.IntegerField(choices=m_Jahrgang)
    Fach = models.IntegerField(choices=m_Fach)
    Schwerpunkt = models.IntegerField(choices=m_Schwerpunkt) #, blank=True)
    Lehrperson = models.CharField(max_length=50)
    Exam = models.FileField()
    

