# Generated by Django 3.2.4 on 2021-10-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_alter_meetup_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]
