from django.core.exceptions import ValidationError

def validate_grade_range(grade):
    error_message = "Ensure this value is less than or equal to 100.0."
    if grade >= 0 and grade <= 100:
        return grade
    else:
        raise ValidationError(error_message, params={'grade' : grade })