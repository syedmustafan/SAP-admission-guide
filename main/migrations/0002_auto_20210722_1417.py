# Generated by Django 2.2.15 on 2021-07-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ranking', models.CharField(max_length=200)),
                ('uniname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('deps', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
                ('relScore', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='accountModel',
            new_name='Account',
        ),
    ]