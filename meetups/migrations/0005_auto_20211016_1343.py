# Generated by Django 3.2.4 on 2021-10-16 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20211016_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
        ),
        migrations.AddField(
            model_name='meetup',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]