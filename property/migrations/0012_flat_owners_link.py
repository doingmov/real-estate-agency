# property/migrations/0012_flat_owners_link.py
from django.db import migrations


def link_flat_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        if flat.owner:
            owner_obj = Owner.objects.filter(name=flat.owner).first()
            if not owner_obj:
                owner_obj = Owner.objects.create(
                    name=flat.owner,
                    phone=flat.owners_phonenumber or ''
                )
            owner_obj.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_flat_to_owner'),
    ]

    operations = [
        migrations.RunPython(link_flat_owners, reverse_code=migrations.RunPython.noop),
    ]