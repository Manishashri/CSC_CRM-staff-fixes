from django.db import migrations, models

import csc_crm.validators


def strip_country_code(apps, schema_editor):
    """Requirement 07: phone numbers are stored as 10 digits (no +91)."""
    Student = apps.get_model('admissions', 'Student')
    for student in Student.objects.all():
        phone = csc_crm.validators.strip_country_code(student.phone_no)
        guardian = csc_crm.validators.strip_country_code(student.guardian_phone_no)
        if (phone, guardian) != (student.phone_no, student.guardian_phone_no):
            student.phone_no = phone
            student.guardian_phone_no = guardian
            student.save(update_fields=['phone_no', 'guardian_phone_no'])


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0007_alter_student_guardian_phone_no_and_more'),
    ]

    operations = [
        migrations.RunPython(strip_country_code, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=13, unique=True, validators=[csc_crm.validators.validate_indian_mobile]),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_phone_no',
            field=models.CharField(max_length=13, unique=True, validators=[csc_crm.validators.validate_indian_mobile]),
        ),
    ]
