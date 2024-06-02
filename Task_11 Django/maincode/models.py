from django.db import models

class Transaction(models.Model):
    date = models.DateField()
    bank = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.date} - {self.bank} - {self.amount}'
