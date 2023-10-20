from django.db import models
class Users(models.Model):
    Firstname=models.CharField(max_length=20)
    Lastname=models.CharField(max_length=20)
    Email=models.EmailField(max_length=250)
    password=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
class childdiseasedetials_2018_19(models.Model):
    District=models.CharField(max_length=20)
    Year=models.CharField(max_length=20)
    pneumonia=models.IntegerField()
    astma=models.IntegerField()
    sephesis=models.IntegerField()
    tetanus=models.IntegerField()
    tuberculosis=models.IntegerField()
class childdiseasedetials_2019_20(models.Model):
    District=models.CharField(max_length=20)
    Year=models.CharField(max_length=20)
    pneumonia=models.IntegerField()
    astma=models.IntegerField()
    sephesis=models.IntegerField()
    tetanus=models.IntegerField()
    tuberculosis=models.IntegerField()
class childdiseasedetials_2017_18(models.Model): 
    District=models.CharField(max_length=20)
    Year=models.CharField(max_length=20)
    pneumonia=models.IntegerField()
    astma=models.IntegerField()
    sephesis=models.IntegerField()
    tetanus=models.IntegerField()
    tuberculosis=models.IntegerField()   
class childvaccinationdetials_2018_19(models.Model):
    District=models.CharField(max_length=20)
    Year=models.CharField(max_length=20)
    opv0=models.IntegerField()
    bcg=models.IntegerField()
    hep_B0=models.IntegerField()
class childvaccinationdetials_2019_20(models.Model):
    District=models.CharField(max_length=20)
    Year=models.CharField(max_length=20)
    opv0=models.IntegerField()
    bcg=models.IntegerField()
    hep_B0=models.IntegerField()    
    

