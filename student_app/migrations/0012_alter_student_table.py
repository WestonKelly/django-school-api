from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0011_alter_student_locker_combination'),
    ]

    operations = [
        migrations.RunSQL('ALTER SEQUENCE student_app_student_id_seq RESTART WITH 1;'),  # Adjust for your DB/backend
    ]