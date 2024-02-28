from django.db import models

class HistoricalData(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.IntegerField()

class StockMarketNews(models.Model):
    source = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    url = models.URLField()
    content = models.TextField()
    image = models.URLField()
