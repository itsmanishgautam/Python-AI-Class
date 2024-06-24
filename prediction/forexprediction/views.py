from django.shortcuts import render
from .models import ForexRate

def forex_rates(request):
    rates = ForexRate.objects.filter(rate_date='2024-06-24')
    return render(request, 'forex_rates.html', {'rates': rates})
