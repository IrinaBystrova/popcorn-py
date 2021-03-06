# Generated by Django 2.1.7 on 2019-05-13 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=200)),
                ('episode_name', models.CharField(max_length=200)),
                ('episode_date', models.DateTimeField()),
                ('download_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date', models.IntegerField()),
                ('genres', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='newitems',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scrapy_app.Series'),
        ),
    ]
