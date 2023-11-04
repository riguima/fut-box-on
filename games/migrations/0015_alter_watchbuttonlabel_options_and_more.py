# Generated by Django 4.2.6 on 2023-11-02 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_remove_watchbutton_game_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchbuttonlabel',
            options={'verbose_name': 'Botão Assistir', 'verbose_name_plural': 'Botões Assistir'},
        ),
        migrations.AlterField(
            model_name='watchbuttonlabel',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Jogo'),
        ),
        migrations.AlterField(
            model_name='watchbuttonlabel',
            name='watch_button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.watchbutton', verbose_name='Botão'),
        ),
    ]