from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all().iterator():
        if flat.owners_phonenumber:
            flat.owner_pure_phone = PhoneNumber.from_string(
                flat.owners_phonenumber,
                region='RU'
            )
            flat.save(update_fields=['owner_pure_phone'])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_previous_migration'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone, reverse_code=migrations.RunPython.noop),
    ]