from django.db import migrations, models

import csc_crm.validators


def strip_country_code(apps, schema_editor):
    """Requirement 07: phone numbers are stored as 10 digits (no +91)."""
    Staff = apps.get_model('staff', 'Staff')
    for staff in Staff.objects.all():
        changed = False
        for field in ('phone', 'emergency_contact_phone'):
            new = csc_crm.validators.strip_country_code(getattr(staff, field))
            if new != getattr(staff, field):
                setattr(staff, field, new)
                changed = True
        if changed:
            staff.save(update_fields=['phone', 'emergency_contact_phone'])


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0023_alter_trainerschedule_options_and_more'),
    ]

    operations = [
        migrations.RunPython(strip_country_code, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=13, unique=True, validators=[csc_crm.validators.validate_indian_mobile]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='emergency_contact_phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[csc_crm.validators.validate_indian_mobile]),
        ),
    ]
