from django.db import models

class ForexRate(models.Model):
    rate_date = models.DateField()
    currency = models.CharField(max_length=50)
    unit = models.IntegerField()
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    sell = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.currency} - {self.rate_date}"
