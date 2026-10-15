from django.db import migrations, models

import csc_crm.validators


def strip_country_code(apps, schema_editor):
    """Requirement 07: phone numbers are stored as 10 digits (no +91)."""
    LeadCapture = apps.get_model('leads', 'LeadCapture')
    for lead in LeadCapture.objects.all():
        new = csc_crm.validators.strip_country_code(lead.phone_no)
        if new != lead.phone_no:
            lead.phone_no = new
            lead.save(update_fields=['phone_no'])


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0015_leadcapturetarget'),
    ]

    operations = [
        migrations.RunPython(strip_country_code, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='leadcapture',
            name='phone_no',
            field=models.CharField(max_length=13, unique=True, validators=[csc_crm.validators.validate_indian_mobile]),
        ),
    ]
