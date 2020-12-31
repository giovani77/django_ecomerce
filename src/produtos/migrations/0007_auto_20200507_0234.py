# Generated by Django 3.1 on 2020-05-07 02:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20200502_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]