from django.shortcuts import render
from rest_framework import viewsets
from . forms import ApprovalForm
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from . models import Customer
from . serializers import CustomerSerializers
from django.contrib import messages
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
        
#@api_view(["POST"])
def Customerreject(X):
    try:
        mdl=joblib.load(open("DT_model.pkl", "rb"))
        #mydata=request.data
        #X=np.array(list(mydata.values()))
        #X=X.reshape(1,-1)
        y_pred=mdl.predict(X)
        newdf=pd.DataFrame(y_pred, columns=['Status'])
        newdf=newdf.replace({1:'Completed', 0:'Not Completed'})
        return (f"{newdf['Status'][0]}")
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

# def result (request, ans):
#     return render(request, 'myform/form.html', {'ans':ans})

def get_request(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
                LP_CustomerPrincipalPayments = form.cleaned_data['LP_CustomerPrincipalPayments']
                LoanMonthsSinceOrigination = form.cleaned_data['LoanMonthsSinceOrigination']
                LP_CustomerPayments = form.cleaned_data['LP_CustomerPayments']
                ClosedDate_day = form.cleaned_data['ClosedDate_day']
                ClosedDate_month = form.cleaned_data['ClosedDate_month']
                EmploymentStatus_Full_time = form.cleaned_data['EmploymentStatus_Full_time']
                Investors = form.cleaned_data['Investors']
                MonthlyLoanPayment = form.cleaned_data['MonthlyLoanPayment']
                LoanOriginationQuarter_Q1_2014 = form.cleaned_data['LoanOriginationQuarter_Q1_2014']
                LoanOriginalAmount = form.cleaned_data['LoanOriginalAmount']
                LoanOriginationQuarter_Q4_2013 = form.cleaned_data['LoanOriginationQuarter_Q4_2013']
                ClosedDate_year = form.cleaned_data['ClosedDate_year']
                DateCreditPulled_year = form.cleaned_data['DateCreditPulled_year']
                LoanOriginationDate_year = form.cleaned_data['LoanOriginationDate_year']
                ListingCreationDate_year = form.cleaned_data['ListingCreationDate_year']

                mydict = (request.POST).dict()
                df = pd.DataFrame(mydict, index = [0])
                ans = Customerreject(df.iloc[:,1:])
                messages.success(request, f'The Loan will be ( {ans} )', )
                #print(ans)
                #result(request, ans)


    form = ApprovalForm()
    return render(request, 'myform/cxform.html', {'form': form})
            