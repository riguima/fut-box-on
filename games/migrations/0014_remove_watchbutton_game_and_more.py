# Generated by Django 4.2.6 on 2023-10-19 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_remove_game_watch_buttons_watchbutton_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchbutton',
            name='game',
        ),
        migrations.RemoveField(
            model_name='watchbutton',
            name='name_in_page',
        ),
        migrations.CreateModel(
            name='WatchButtonLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Nome na página')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('watch_button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.watchbutton')),
            ],
        ),
    ]