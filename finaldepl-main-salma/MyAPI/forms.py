from django import forms

class ApprovalForm(forms.Form):
    Customer_Principal_Payments = forms.IntegerField()
    Loan_Months_Since_Origination = forms.IntegerField()
    Customer_Payments = forms.IntegerField()
    Employment_Status_Full_time = forms.ChoiceField(choices = [(0, "Not Full Time"), (1, "Full Time")])
    Investors = forms.IntegerField()
    Monthly_Loan_Payment = forms.IntegerField()
    Loan_Original_Amount = forms.IntegerField()