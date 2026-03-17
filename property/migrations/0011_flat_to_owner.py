from django.db import migrations
from phonenumber_field.phonenumber import PhoneNumber


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        phone_pure = flat.owner_pure_phone
        if phone_pure:
            owner_obj = Owner.objects.filter(phone_pure=phone_pure).first()
            if not owner_obj:
                owner_obj = Owner.objects.create(
                    name=flat.owner or '',
                    phone=flat.owners_phonenumber or '',
                    phone_pure=phone_pure
                )
            owner_obj.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_fill_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(create_owners, reverse_code=migrations.RunPython.noop),
    ]