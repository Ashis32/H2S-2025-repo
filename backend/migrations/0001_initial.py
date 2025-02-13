# Generated by Django 4.2.13 on 2024-06-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradingRubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.CharField(blank=True, max_length=50)),
                ('level', models.CharField(blank=True, max_length=20)),
                ('language', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('content', models.FileField(upload_to='rubrics')),
                ('last_updated', models.DateTimeField()),
                ('writing_type', models.CharField(choices=[('C', 'Creative Writing'), ('A', 'Academic Writing'), ('E', 'Expository Writing'), ('D', 'Descriptive'), ('N', 'Narrative'), ('O', 'Other'), ('U', 'Unspecified')], default='U', max_length=1)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
