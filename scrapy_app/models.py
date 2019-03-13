from django.db import models


class Series(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.IntegerField()
    genres = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class NewItems(models.Model):
    series_name = models.CharField(max_length=200)
    episode_name = models.CharField(max_length=200)
    episode_date = models.DateTimeField()
    download_link = models.CharField(max_length=200)
    # series = models.ForeignKey('Series', on_delete=models.SET_NULL,
    #                            null=True)

    def __str__(self):
        return self.series_name
