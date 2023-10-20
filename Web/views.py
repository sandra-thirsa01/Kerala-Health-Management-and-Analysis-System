from tkinter import messagebox
from django.shortcuts import render
import mysql.connector as sql
from .forms import HForm,ChildDisease,ChildVaccination,UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import childdiseasedetials_2019_20,childdiseasedetials_2018_19,childvaccinationdetials_2018_19,childvaccinationdetials_2019_20,Users
def index(request):
    return render(request,'web/home.html')
em=''
pwd=''
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
                em=form.cleaned_data['email']
                pwd=form.cleaned_data['password']
        m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database='website')
        cursor=m.cursor() 
        c="select * from web_users where Email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
          
            return HttpResponseRedirect("error")
            
        else:
            return HttpResponseRedirect('welcome')
            
    form=UserForm()
    return render(request,'web/login.html',{'forms':form})
    # global em,pwd
    # if request.method=="POST":
    #     m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database='website')
    #     cursor=m.cursor()
    #     d=request.POST
    #     for key,value in d.items():
    #         if key=="email":
    #             em=value
    #         if key=="password":
    #             pwd=value
        
    #     c="select * from users where email='{}' and password='{}'".format(em,pwd)
    #     cursor.execute(c)
    #     t=tuple(cursor.fetchall())
    #     if t==():
    #         return render(request,'web/error.html')
    #     else:
    #         return HttpResponseRedirect('welcome')
    #         # fname=t[0][0].upper()
    #         # lname=t[0][1].upper()
    #         # form=HForm()
    #         # return render(request,"web/welcome.html",{"firstname":fname,"lastname":lname,"forms":form})

    # return render(request,'web/login.html')
def welcomeaction(request):

            if request.method=='POST':
                form=HForm(request.POST)
                if form.is_valid():
                    print(form.cleaned_data['category'])
                    if form.cleaned_data['category']=='childdisease':
                         return HttpResponseRedirect('child disease')
                    elif form.cleaned_data['category']=='childvaccination':
                         return HttpResponseRedirect('child vaccination') 

            m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database='website')
            cursor=m.cursor()
            c="select * from web_users where Email='{}' and password='{}'".format(em,pwd)
            cursor.execute(c)
            t=tuple(cursor.fetchall())
            fname=t[0][1].upper()
            lname=t[0][2].upper()
            form=HForm()
            return render(request,"web/welcome.html",{"firstname":fname,"lastname":lname,"forms":form})
district=''
year=''
def childdisease(request):
    global district,year
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database='website')
        cursor=m.cursor()
        form=ChildDisease(request.POST)       
        d=request.POST
        for key,value in d.items():
            if key=="district":
                district=value
            if key=="year":
                year=value      
        if form.is_valid():
           if form.cleaned_data['year']=='2018-19':
              c="select pneumonia,astma,sephesis,tetanus,tuberculosis from web_childdiseasedetials_2018_19 where District='{}' and Year='{}'".format(district,year)
              cursor.execute(c)
              t=tuple(cursor.fetchall())
              npneumonia=t[0][0]+form.cleaned_data['pneumonia']
              nastma=t[0][1]+form.cleaned_data['Astma']
              nsephesis=t[0][2]+form.cleaned_data['Sephesis']
              ntetanus=t[0][3]+form.cleaned_data['Tetanus']
              ntuberculosis=t[0][4]+form.cleaned_data['Tuberculosis']
              childdiseasedetials_2018_19.objects.filter(District=district).update(pneumonia=npneumonia,astma=nastma,sephesis=nsephesis,tetanus=ntetanus,tuberculosis=ntuberculosis)
           elif form.cleaned_data['year']=='2019-20':
              c="select pneumonia,astma,sephesis,tetanus,tuberculosis from web_childdiseasedetials_2019_20 where District='{}' and Year='{}'".format(district,year)
              cursor.execute(c)
              t=tuple(cursor.fetchall())
              npneumonia=t[0][0]+form.cleaned_data['pneumonia']
              nastma=t[0][1]+form.cleaned_data['Astma']
              nsephesis=t[0][2]+form.cleaned_data['Sephesis']
              ntetanus=t[0][3]+form.cleaned_data['Tetanus']
              ntuberculosis=t[0][4]+form.cleaned_data['Tuberculosis']
              childdiseasedetials_2019_20.objects.filter(District=district).update(pneumonia=npneumonia,astma=nastma,sephesis=nsephesis,tetanus=ntetanus,tuberculosis=ntuberculosis)
              return HttpResponse('Thankyou for your response.your response has been submitted successfully')
    form=ChildDisease()
    return render(request,'web/childdiseaseform.html',{'forms':form})
    
def childvaccination(request):
    global district,year
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database='website')
        cursor=m.cursor()
        form=ChildVaccination(request.POST)            
        d=request.POST
        for key,value in d.items():
            if key=="district":
                district=value
            if key=="year":
                year=value     
        if form.is_valid():
           if form.cleaned_data['year']=='2018-19':
              b="select opv0, bcg,hep_B0 from web_childvaccinationdetials_2018_19 where District='{}' and Year='{}'".format(district,year)
              cursor.execute(b)
              t=tuple(cursor.fetchall())
              nopv0=t[0][0]+form.cleaned_data['opv0']
              nbcg=t[0][1]+form.cleaned_data['bcg']
              nhep_B0=t[0][2]+form.cleaned_data['hep_B0']
              childvaccinationdetials_2018_19.objects.filter(District=district).update(opv0=nopv0,bcg=nbcg,hep_B0 =nhep_B0)
           elif form.cleaned_data['year']=='2019-20':
              b="select opv0, bcg,hep_B0 from web_childvaccinationdetials_2019_20  where District='{}' and Year='{}'".format(district,year)
              cursor.execute(b)
              t=tuple(cursor.fetchall())
              nopv0=t[0][0]+form.cleaned_data['opv0']
              nbcg=t[0][1]+form.cleaned_data['bcg']
              nhep_B0=t[0][2]+form.cleaned_data['hep_B0']
              childvaccinationdetials_2019_20.objects.filter(District=district).update(opv0=nopv0,bcg=nbcg,hep_B0 =nhep_B0)
              return HttpResponse('Thank you for your response your response has been submitted successfully')
    form=ChildVaccination()
    return render(request,'web/childimmunisation.html',{'forms':form})    
    


