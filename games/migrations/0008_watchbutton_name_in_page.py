# Generated by Django 4.2.6 on 2023-10-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_watchbutton_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchbutton',
            name='name_in_page',
            field=models.CharField(default=''),
        ),
    ]
