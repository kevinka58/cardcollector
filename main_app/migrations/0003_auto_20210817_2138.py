# Generated by Django 3.2.6 on 2021-08-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cardset'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardset',
            name='condition',
            field=models.CharField(choices=[('1', 'PSA-1'), ('2', 'PSA-2'), ('3', 'PSA-3'), ('4', 'PSA-4'), ('5', 'PSA-5'), ('6', 'PSA-6'), ('7', 'PSA-7'), ('8', 'PSA-8'), ('9', 'PSA-9'), ('10', 'PSA-10')], default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='cardset',
            name='rarity',
            field=models.CharField(default='Common', max_length=100),
        ),
        migrations.AddField(
            model_name='cardset',
            name='status',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
