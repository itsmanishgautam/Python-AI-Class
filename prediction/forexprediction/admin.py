from django.contrib import admin

# Register your models here.
from .models import HistoricalForexData

admin.site.register(HistoricalForexData)
