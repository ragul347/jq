# Generated by Django 3.0.3 on 2020-12-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quizques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=10)),
                ('question_no', models.CharField(max_length=3)),
                ('questions', models.CharField(max_length=500)),
                ('a', models.CharField(max_length=50)),
                ('b', models.CharField(max_length=50)),
                ('c', models.CharField(max_length=50)),
                ('d', models.CharField(max_length=50)),
                ('ans', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=100)),
            ],
        ),
    ]
