# Generated by Django 2.1.7 on 2019-03-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popcorn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newitems',
            name='download_link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newitems',
            name='episode_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='newitems',
            name='episode_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newitems',
            name='series_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='series',
            name='date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='series',
            name='genres',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='series',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]