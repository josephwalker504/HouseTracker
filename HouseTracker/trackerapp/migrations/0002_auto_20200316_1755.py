# Generated by Django 3.0.4 on 2020-03-16 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.CharField(max_length=50, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='house',
            name='investorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trackerapp.Investor'),
        ),
    ]
