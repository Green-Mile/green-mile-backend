# Generated by Django 3.1.4 on 2021-01-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.IntegerField(choices=[(1, 'WITH SUPLIER'), (2, 'AT GREEN MILE HUB'), (3, 'REBUNDLING'), (4, 'ON FLEET'), (5, 'DELIVERED')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='package',
            name='type',
            field=models.IntegerField(choices=[(1, 'Envelope'), (2, 'Parcel'), (3, 'Soft'), (4, 'Freezed')], default=1, max_length=1),
        ),
    ]
