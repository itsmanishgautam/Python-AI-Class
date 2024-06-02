from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_success')
    else:
        form = TransactionForm()
    return render(request, 'user_input/form.html', {'form': form})

def transaction_success(request):
    return render(request, 'user_input/success.html')
