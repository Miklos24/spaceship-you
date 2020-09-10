# Generated by Django 3.1.1 on 2020-09-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('couch_alotted', models.IntegerField()),
                ('couch_used', models.IntegerField()),
                ('exercise_alotted', models.IntegerField()),
                ('exercise_used', models.IntegerField()),
                ('creative_allotted', models.IntegerField()),
                ('creative_used', models.IntegerField()),
                ('sleep_alotted', models.IntegerField()),
                ('sleep_used', models.IntegerField()),
            ],
        ),
    ]