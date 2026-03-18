from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_fill_owner_from_flat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone',
        ),
    ]