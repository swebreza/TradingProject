from datetime import datetime
from django.db import models

# Create your models here.

class Candle(models.Model):
 bank_nifty = models.CharField(max_length=255)
 open_trade=models.FloatField()
 close_trade=models.FloatField()
 high_trade=models.FloatField()
 low_trade=models.FloatField()
 date_of_trade = models.DateField(blank=True)
