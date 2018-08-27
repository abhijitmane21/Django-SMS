# Generated by Django 2.1 on 2018-08-23 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('duration', models.IntegerField()),
                ('deartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Department')),
            ],
        ),
    ]