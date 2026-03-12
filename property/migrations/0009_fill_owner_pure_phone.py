from django.db import migrations
import phonenumbers


def normalize_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        raw_phone = flat.owners_phonenumber
        if not raw_phone:
            continue
        try:
            parsed = phonenumbers.parse(raw_phone, 'RU')
            if phonenumbers.is_valid_number(parsed):
                flat.owner_pure_phone = phonenumbers.format_number(
                    parsed, phonenumbers.PhoneNumberFormat.E164)
                flat.save(update_fields=['owner_pure_phone'])
            else:
                flat.owner_pure_phone = None
                flat.save(update_fields=['owner_pure_phone'])
        except phonenumbers.NumberParseException:
            flat.owner_pure_phone = None
            flat.save(update_fields=['owner_pure_phone'])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_owner_pure_phone),
    ]