from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from web.models import *
from .forms import Dashboards,CvrDashboard
def childdiseasereport(request):
    item1=childdiseasedetials_2018_19.objects.all().values()
    item2=childdiseasedetials_2019_20.objects.all().values()
    df=pd.DataFrame(item1)
    df1=pd.DataFrame(item2)
    df3=pd.concat([df,df1])
    df2= df3.groupby(['Year'], as_index=False).agg({'pneumonia':'sum', 'astma':'sum', 'sephesis':'sum', 'tetanus':'sum','tuberculosis':'sum'})
    a=df2['pneumonia'].sum()
    b=df2['astma'].sum()
    c=df2['sephesis'].sum()
    d=df2['tetanus'].sum()
    e=df2['tuberculosis'].sum()
    total=a+b+c+d+e
    na=int((a/total)*100)
    nb=int((b/total)*100)
    nc=int((c/total)*100)
    nd=int((d/total)*100)
    ne=int((e/total)*100)
    data=[na,nb,nc,nd,ne]
    label=['pneumonia','astma','sephesis','tetanus','tuberculosis']
    if request.method=="POST":
           forms=Dashboards(request.POST)
           if forms.is_valid():
             diseasename=forms.cleaned_data['disease']
             year=list(df2['Year'].values)
             disease=list(df2[diseasename].values)
             return render(request,"report/piechart.html",{'form':forms,'data':data,'label':label,'data1':disease,'label1':year})
    forms=Dashboards()
    data1=[a,b,c,d,e]
    label1=['pneumonia','astma','sephesis','tetanus','tuberculosis']         
    return render(request,"report/piechart.html",{'form':forms,'data':data,'label':label,'data1':data1,'label1':label1})
dict={'Alappuzha':0,"Ernakulam":1, "Idukki":2, "Kannur":3,"Kasaragod":4,"Kollam":5,"Kottayam":6,"Kozhikkode":7,
"Malappuram":8,"Palakkad":9 ,"Pathanamthitta":10,"Thiruvananthapuram":11,"Thrissur":12,"Wayanad":13}    
   
def cvr(request):
    item1=childvaccinationdetials_2018_19.objects.all().values()
    item2=childvaccinationdetials_2019_20.objects.all().values()
    df=pd.DataFrame(item1)
    df1=pd.DataFrame(item2)
    df3=pd.concat([df,df1])
    df2= df3.groupby(['District'], as_index=False).agg({'opv0':'sum', 'bcg':'sum', 'hep_B0':'sum'})
    label=list(df2['District'].values)
    data=list(df2['opv0'].values)
    if request.method=="POST":
           forms=CvrDashboard(request.POST)
           if forms.is_valid():
             vaccination=forms.cleaned_data['vaccine']
             label=list(df2['District'].values)
             data=list(df2[vaccination].values)
             return render(request,"report/childvaccinationreport.html",{'vaccine':vaccination,'form':forms,'data':data,'label':label})
    forms=CvrDashboard()
    vaccination="Opv0"        
    return render(request,"report/childvaccinationreport.html",{'vaccine':vaccination,'form':forms,'data':data,'label':label})



