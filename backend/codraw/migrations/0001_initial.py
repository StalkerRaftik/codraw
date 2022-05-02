from django.conf import settings
from django.db import migrations


def create_superuser(apps, schema_editor):
    apps.get_model('auth', 'User').objects.create_superuser(
        'admin',
        'admin@myproject.com',
        'admin'
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop),
    ]
