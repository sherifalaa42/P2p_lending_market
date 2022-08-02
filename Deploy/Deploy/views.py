from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
import pickle
def home(request):
    return render(request,"home.html")

def result(request):
    cls = pickle.load(open('model.pkl','rb'))
    lis = []
    lis.append(request.GET['LP_CustomerPrincipalPayments'])
    lis.append(request.GET['LoanMonthsSinceOrigination'])
    lis.append(request.GET['LP_CustomerPayments'])
    lis.append(request.GET['ClosedDate_day'])
    lis.append(request.GET['ClosedDate_month'])
    lis.append(request.GET['EmploymentStatus_Full_time'])
    lis.append(request.GET['Investors'])
    lis.append(request.GET['MonthlyLoanPayment'])
    lis.append(request.GET['LoanOriginationQuarter_Q1_2014'])
    lis.append(request.GET['LoanOriginalAmount'])
    lis.append(request.GET['LoanOriginationQuarter_Q4_2013'])
    lis.append(request.GET['ClosedDate_year'])
    lis.append(request.GET['DateCreditPulled_year'])
    lis.append(request.GET['LoanOriginationDate_year'])
    lis.append(request.GET['ListingCreationDate_year'])
    
    ans =cls.predict([lis])

    return render(request,"result.html",{'ans':ans})