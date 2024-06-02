import datetime
from django import forms
from .models import Transaction
import csv

# Helper function to read bank names from CSV
def get_bank_choices():
    bank_choices = []
    csv_path = "csv/bank.csv"
    
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bank_choices.append((row['Bank Name'], row['Bank Name']))
    
    return bank_choices

class TransactionForm(forms.ModelForm):
    # Calculate the range of years for the SelectDateWidget
    current_year = datetime.date.today().year
    year_range = range(current_year - 5, current_year + 7)

    date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=year_range,
            empty_label=("Choose Year", "Choose Month", "Choose Day")
        ),
        input_formats=['%Y-%m-%d']
    )

    bank = forms.ChoiceField(choices=get_bank_choices())

    amount = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ['date', 'bank', 'amount']
