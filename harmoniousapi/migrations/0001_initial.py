# Generated by Django 4.1.6 on 2023-03-07 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rootNote', models.CharField(max_length=20)),
                ('quality', models.CharField(max_length=20)),
                ('texture1filepath', models.CharField(max_length=200)),
                ('texture2filepath', models.CharField(max_length=200)),
                ('texture3filepath', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChordProgression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('firstChord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firstChord', to='harmoniousapi.chord')),
                ('fourthChord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fourthChord', to='harmoniousapi.chord')),
                ('secondChord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondChord', to='harmoniousapi.chord')),
                ('thirdChord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thirdChord', to='harmoniousapi.chord')),
            ],
        ),
        migrations.CreateModel(
            name='MelodyTexture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('synthSetting1', models.IntegerField()),
                ('synthSetting2', models.IntegerField()),
                ('synthSetting3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Soundscape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('chordTexture', models.IntegerField()),
                ('melodyNotes', models.CharField(max_length=50)),
                ('melodyTexture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harmoniousapi.melodytexture')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SoundscapeChordProgression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chordProgression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harmoniousapi.chordprogression')),
                ('soundscape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harmoniousapi.soundscape')),
            ],
        ),
        migrations.AddField(
            model_name='soundscape',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harmoniousapi.user'),
        ),
    ]
