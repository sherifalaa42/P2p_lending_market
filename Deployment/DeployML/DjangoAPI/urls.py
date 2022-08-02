"""DeployML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re
from django.shortcuts import render

# Create your views here.
from .froms import CustomerForm 
# import froms
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import Customer
# from .serializers import CustomerSerializers 
import serializers
import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 

class CustomerView(viewsets.ModelViewSet): 
    queryset = Customer.objects.all() 
    serializer_class = serializers.CustomerSerializers 

def status(df):
    try:
        model=pickle.load(open("D:\Projects\lending_market\Deployment\DeployML\DjangoAPI\Decision_Tree.sav", 'rb'))

        y_pred = model.predict(df)  
        result = "Completed" if y_pred == 1 else "Not Completed"
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView(request):
    if request.method=='POST':
        form=CustomerForm(request.POST or None)

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
            df=pd.DataFrame({'LP_CustomerPrincipalPayments':[LP_CustomerPrincipalPayments], 'LoanMonthsSinceOrigination':[LoanMonthsSinceOrigination],
            'LP_CustomerPayments':[LP_CustomerPayments],'ClosedDate_day':[ClosedDate_day],'ClosedDate_month':[ClosedDate_month],
            'EmploymentStatus_Full_time':[EmploymentStatus_Full_time],
            'Investors':[Investors],'MonthlyLoanPayment':[MonthlyLoanPayment],'LoanOriginationQuarter_Q1_2014':[LoanOriginationQuarter_Q1_2014],
            'LoanOriginalAmount':[LoanOriginalAmount],'LoanOriginationQuarter_Q4_2013':[LoanOriginationQuarter_Q4_2013],
            'ClosedDate_year':[ClosedDate_year],'DateCreditPulled_year':[DateCreditPulled_year],
            'LoanOriginationDate_year':[LoanOriginationDate_year],'ListingCreationDate_year':[ListingCreationDate_year]})
            df["Status"] = 1 if "Completed" else 0
            result = status(df)
            return render(request, 'status.html', {"data": result}) 
            
    form=CustomerForm()
    return render(request, 'form.html', {'form':form})

from turtle import home
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
                path('api/', include(router.urls)),
                path('form/', FormView, name='form'),
                
              ]
