# Generated by Django 2.2.2 on 2019-07-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0011_auto_20190714_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='hash_code',
            field=models.CharField(default='3x8HLmUzXE5IaH1IJyY4XL3rBFkrVLzBXTEMTlEs25cl6qU479koE578LxDh0Wtu', max_length=64, unique=True),
        ),
    ]
