from django.db import migrations

def forwards_func(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        if flat.owner:
            owner_obj, created = Owner.objects.get_or_create(
                name=flat.owner,
                phone=flat.owners_phonenumber
            )
            

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]