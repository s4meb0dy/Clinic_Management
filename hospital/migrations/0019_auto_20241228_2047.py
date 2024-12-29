

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('General Practitioners', 'General Practitioners'), ('Pediatricians', 'Pediatricians'), ('ESurgeons', 'Surgeons'), ('Cardiologists', 'Cardiologists'), ('Neurologists', 'Neurologists'), ('Gynecologists', 'Gynecologists'), ('Ophthalmologists', 'Ophthalmologists'), ('Dermatologists', 'Dermatologists'), ('Psychiatrists', 'Psychiatrists')], default='Cardiologist', max_length=50),
        ),
    ]
