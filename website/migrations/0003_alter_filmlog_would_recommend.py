# Generated by Django 5.1.3 on 2024-12-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_filmlog_delete_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmlog',
            name='would_recommend',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]