# Generated by Django 3.1 on 2020-04-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to='produtos/'),
        ),
    ]
