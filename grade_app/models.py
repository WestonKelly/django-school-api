from django.db import models
from django.core import validators as v
from student_app.models import Student
from subject_app.models import Subject
from .validators import validate_grade_range

class Grade(models.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=False, unique=False, default=100, validators=[validate_grade_range])
    a_subject = models.ForeignKey(Subject, related_name="grades", null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, related_name="grades", null=True, on_delete=models.SET_NULL)



