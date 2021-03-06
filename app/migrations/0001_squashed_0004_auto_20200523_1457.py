# Generated by Django 3.0.6 on 2020-05-25 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_auto_20200523_0150'), ('app', '0003_auto_20200523_1443'), ('app', '0004_auto_20200523_1457')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=20)),
                ('django', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='telegram', to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=150)),
                ('link', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('chat_id', models.CharField(max_length=20)),
                ('members', models.ManyToManyField(related_name='guilds', to='app.TelegramUser')),
            ],
        ),
        migrations.CreateModel(
            name='InfluenceCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.DateTimeField()),
                ('notification_job_id', models.CharField(max_length=30)),
                ('waiting_to_notify', models.BooleanField(default=True)),
                ('notified', models.BooleanField(default=False)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.TelegramUser')),
                ('in_guild', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Guild')),
            ],
        ),
    ]
