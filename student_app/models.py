from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(default=None,max_length=255, blank = False)
    student_email = models.EmailField(max_length=100, unique=True, default=None, blank=False)
    personal_email = models.EmailField(max_length=100, null=True, unique=True, default=None)
    locker_number = models.IntegerField(default=110, unique=True)
    locker_combination = models.CharField(max_length=8, blank=False, default="12-12-12")
    good_student = models.BooleanField(default=True, unique=False)

    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    def locker_reassignment(self):
        self.locker_number = input("Enter new locker number")
        self.save()

    def student_status(self):
        status = input("Enter 'True' of 'False' for status")
        if status == "True":
            status = True
        else:
            status = False
        self.good_student = status
        self.save()


# default=None unique=True
# requirements.txt 
# pip freeze > requirements.txt
# python manage.py test