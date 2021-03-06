# Generated by Django 3.2.6 on 2021-08-17 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cardset_card_set_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardset',
            name='rarity',
            field=models.CharField(choices=[('1', 'Common'), ('2', 'Uncommon'), ('3', 'Rare'), ('4', 'Holo Rare'), ('5', 'Reverse Holo'), ('6', 'Secret Rare'), ('7', 'Rainbow Rare'), ('8', 'Promotional'), ('9', 'Does Not Apply')], default='Common', max_length=100),
        ),
        migrations.AlterField(
            model_name='cardset',
            name='status',
            field=models.CharField(choices=[('1', 'EX'), ('2', 'GX'), ('3', 'Tag Team'), ('4', 'VMAX'), ('5', 'Full Art'), ('6', 'Full Body'), ('7', 'Half Art'), ('8', 'Half Body '), ('9', 'V'), ('10', 'Does Not Apply')], default='Ex: Full-Art, Half-Art, etc...', max_length=100),
        ),
    ]
