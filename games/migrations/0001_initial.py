# Generated by Django 4.2.9 on 2024-01-26 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='nome')),
                ('image_url', models.CharField(verbose_name='url da imagem')),
            ],
            options={
                'verbose_name': 'Campeonato',
                'verbose_name_plural': 'Campeonatos',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(verbose_name='cabeçalho')),
            ],
            options={
                'verbose_name': 'Configuração',
                'verbose_name_plural': 'Configurações',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='inicio')),
                ('end_time', models.TimeField(verbose_name='final')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.championship', verbose_name='campeonato')),
            ],
            options={
                'verbose_name': 'Jogo',
                'verbose_name_plural': 'Jogos',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='nome')),
                ('image_url', models.CharField(verbose_name='url da imagem')),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.CreateModel(
            name='WatchButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='nome')),
                ('url', models.CharField()),
            ],
            options={
                'verbose_name': 'Botão Assistir',
                'verbose_name_plural': 'Botões Assistir',
            },
        ),
        migrations.CreateModel(
            name='WatchButtonLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Nome na página')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Jogo')),
                ('watch_button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.watchbutton', verbose_name='Botão')),
            ],
            options={
                'verbose_name': 'Botão Assistir',
                'verbose_name_plural': 'Botões Assistir',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='games.team', verbose_name='time mandante'),
        ),
        migrations.AddField(
            model_name='game',
            name='visiting_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visiting_team', to='games.team', verbose_name='time visitante'),
        ),
    ]
