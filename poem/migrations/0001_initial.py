# Generated by Django 2.2.5 on 2021-03-14 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('author_info', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Dynasty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dynasty', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('annotation', models.TextField(blank=True, default='')),
                ('translation', models.TextField(blank=True, default='')),
                ('background', models.TextField(blank=True, default='')),
                ('remark', models.TextField(blank=True, default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Author')),
                ('dynasty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Dynasty')),
            ],
        ),
    ]
