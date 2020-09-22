# Generated by Django 3.0.10 on 2020-09-22 16:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='contenido')),
                ('ordering', models.SmallIntegerField(default=0, verbose_name='orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'verbose_name': 'página',
                'verbose_name_plural': 'páginas',
                'ordering': ['ordering', 'title'],
            },
        ),
    ]
