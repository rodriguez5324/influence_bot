# Generated by Django 3.0.6 on 2020-05-31 12:51

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0001_squashed_0004_auto_20200523_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('time', models.DateTimeField()),
                ('job_id', models.CharField(max_length=30)),
                ('canceled', models.BooleanField(default=False)),
                ('notified', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(app.models.ActionMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='last_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='InfluenceCollection',
        ),
    ]
