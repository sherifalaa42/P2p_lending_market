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
        mdl=joblib.load(open("MyAPI/DT_model.pkl", "rb"))
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
                Customer_Principal_Payments = form.cleaned_data['Customer_Principal_Payments']
                Loan_Months_Since_Origination = form.cleaned_data['Loan_Months_Since_Origination']
                Customer_Payments = form.cleaned_data['Customer_Payments']
                Employment_Status_Full_time = form.cleaned_data['Employment_Status_Full_time']
                Investors = form.cleaned_data['Investors']
                Monthly_Loan_Payment = form.cleaned_data['Monthly_Loan_Payment']
                Loan_Original_Amount = form.cleaned_data['Loan_Original_Amount']
        
                
                mydict = (request.POST).dict()
                df = pd.DataFrame(mydict, index = [0])
                ans = Customerreject(df.iloc[:,1:])
                messages.success(request, f'The Loan will be ( {ans} )', )
                #print(ans)
                #result(request, ans)


    form = ApprovalForm()
    return render(request, 'myform/cxform.html', {'form': form})
            