from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber

def forwards(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        if not flat.owner_name:
            continue

        phone_pure = PhoneNumber.from_string(flat.owner_phone, region='RU') if flat.owner_phone else None

        owner_obj, created = Owner.objects.get_or_create(
            name=flat.owner_name or '',
            defaults={
                'phone': flat.owner_phone or '',
                'phone_pure': phone_pure
            }
        )

        owner_obj.flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_remove_complaint_user_remove_flat_owner_and_more'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]