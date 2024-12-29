

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20241228_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='admitDate',
            field=models.DateField(null=True),
        ),
    ]
