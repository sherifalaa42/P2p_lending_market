from django import forms
# from .models import Customer
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
              model = Customer
              fields = "__all__"

    LP_CustomerPrincipalPayments = forms.IntegerField()
    LoanMonthsSinceOrigination = forms.IntegerField()
    LP_CustomerPayments = forms.IntegerField()
    ClosedDate_day = forms.IntegerField()
    ClosedDate_month = forms.IntegerField()
    EmploymentStatus_Full_time = forms.IntegerField()
    Investors = forms.IntegerField()
    MonthlyLoanPayment = forms.IntegerField()
    LoanOriginationQuarter_Q1_2014 = forms.IntegerField()
    LoanOriginalAmount = forms.IntegerField()
    LoanOriginationQuarter_Q4_2013 = forms.IntegerField()
    ClosedDate_year = forms.IntegerField()
    DateCreditPulled_year = forms.IntegerField()
    LoanOriginationDate_year = forms.IntegerField()
    ListingCreationDate_year = forms.IntegerField()