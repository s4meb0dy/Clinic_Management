

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_auto_20241228_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('General Practitioners', 'General Practitioners'), ('Pediatricians', 'Pediatricians'), ('Surgeons', 'Surgeons'), ('Cardiologists', 'Cardiologists'), ('Neurologists', 'Neurologists'), ('Gynecologists', 'Gynecologists'), ('Ophthalmologists', 'Ophthalmologists'), ('Dermatologists', 'Dermatologists'), ('Psychiatrists', 'Psychiatrists')], default='General Practitioners', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='admitDate',
            field=models.DateField(),
        ),
    ]
