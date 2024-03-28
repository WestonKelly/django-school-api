from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import validate_name_format, validate_school_email, validate_combination_format

# Create your models here.

class Student(models.Model):
    name = models.CharField(default=None,max_length=255, blank = False, validators=[validate_name_format])
    student_email = models.EmailField(max_length=100, unique=True, default=None, blank=False, validators=[validate_school_email])
    personal_email = models.EmailField(max_length=100, null=True, unique=True, default=None)
    locker_number = models.IntegerField(default=110, unique=True, blank=False, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(blank=False, default="12-12-12", validators=[validate_combination_format])
    good_student = models.BooleanField(default=True, unique=False)
    subjects = models.ManyToManyField('subject_app.Subject', related_name='students')

    
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

    def add_subject(self, subject_id):
        error_message = "This students class schedule is full!"
        subject_length = self.subjects.count()
        if subject_length < 8:
            self.subjects.add(subject_id)
        else:
            raise Exception(error_message)

    def remove_subject(self, subject_id):
        error_message = "This students class schedule is empty!"
        if self.subjects.exists():
            subject = self.subjects.get(pk=subject_id)
            self.subjects.remove(subject)
        else:
            raise Exception(error_message)



        



# default=None unique=True
# requirements.txt 
# pip freeze > requirements.txt
# python manage.py test