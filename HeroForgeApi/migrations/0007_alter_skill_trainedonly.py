# Generated by Django 4.0.3 on 2022-03-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeroForgeApi', '0006_alter_skill_trainedonly'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='trainedOnly',
            field=models.BooleanField(default=False),
        ),
    ]
