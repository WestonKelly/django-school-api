from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from django.apps import apps
from .validators import validate_subject_format, validate_professor_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=50, blank=False, null=False, unique=True, validators=[validate_subject_format])
    professor = models.CharField(max_length=50, blank=False, null=False, default="Mr. Cahan", validators=[validate_professor_name])
    # students = models.ManyToManyField('student_app.Student', related_name='subjects')

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students}"
    
    def add_a_student(self, student_id):
        Student = apps.get_model('student_app', 'Student')
        student = Student.objects.get(pk=student_id)
        max_students = 30
        if self.students.count() < max_students:
            self.students.add(student)
        else:
            raise ValidationError("This subject id full!")

    def drop_a_student(self, student_id):
        error_message = "This subject is empty!"
        if self.students.exists():
            Student = apps.get_model('student_app', 'Student')
            student = Student.objects.get(pk=student_id)
            self.students.remove(student)
            student.grades.filter(subject=self).delete()
        else:
            raise Exception(error_message)
