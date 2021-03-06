# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-25 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0005_parent_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('P', 'P'), ('A', 'A')], max_length=1)),
                ('remark', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('batch', models.CharField(max_length=80)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField()),
                ('exam_date', models.DateTimeField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(choices=[('FY', 'FY'), ('SY', 'SY'), ('TY', 'TY')], max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='school.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examsubject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
        migrations.AddField(
            model_name='examsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
    ]
