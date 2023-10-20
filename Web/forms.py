from unittest.util import _MAX_LENGTH
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
c= [
    ('childdisease', 'Child Disease'),
    ('childvaccination', 'Child Vaccinaion'),
    ('maternal health', 'Maternal Health'),
    ]
d=[('Alappuzha','Alappuzha'),
('Ernakulam','Ernakulam'),('Idukki','Idukki'),('Kannur','Kannur'),('Kasaragod','Kasaragod'),('Kollam','Kollam'),
('Kottayam','Kottayam'),('Malappuram','Malappuram'),('Palakkad','Palakkad'),('Pathanamthitta','Pathanamthitta'),('Thiruvananthapuram','Thiruvananthapuram'),('Thrissur','Thrissur'),('Wayanad','Wayanad'),('Kozhikkode','Kozhikkode')]
y=[('2019-20','2019-20'),('2018-19','2018-19')]
class UserForm(forms.Form):
    attrs={"type":"password"}
    email=forms.EmailField(max_length=250)
    password=forms.CharField(widget=forms.TextInput(attrs=attrs))
class HForm(forms.Form):
    category=forms.CharField(label='Choose Category', widget=forms.Select(choices=c))
class ChildDisease(forms.Form):
    district=forms.CharField(label='Choose the district',widget=forms.Select(choices=d),required=True)
    year=forms.CharField(label='Choose the Year',widget=forms.Select(choices=y),required=True)
    pneumonia=forms.IntegerField(label='Number of childrens within 0-5 years old reported with pneumonia',required=True) 
    Astma=forms.IntegerField(label='Number of childrens within 0-5 years old reported with Astma',validators=[MinValueValidator(0)],required=True)
    Sephesis=forms.IntegerField(label='Number of childrens within 0-5 years old reported with Sephesis',validators=[MinValueValidator(0)],required=True)
    Tetanus=forms.IntegerField(label='Number of childrens within 0-5 years old reported with Tetanus',validators=[MinValueValidator(0)],required=True)
    Tuberculosis=forms.IntegerField(label='Number of childrens within 0-5 years old reported with Tuberculosis',validators=[MinValueValidator(0)],required=True)   
class ChildVaccination(forms.Form):
    district=forms.CharField(label='Choose the district',widget=forms.Select(choices=d),required=True)
    year=forms.CharField(label='Choose the Year',widget=forms.Select(choices=y),required=True)
    opv0=forms.IntegerField(label='Number of infants given OPV 0',validators=[MinValueValidator(0)],required=True)
    bcg=forms.IntegerField(label='Number of infants given BCG',validators=[MinValueValidator(0)],required=True)
    hep_B0=forms.IntegerField(label='Number of infants given HEP-B0',validators=[MinValueValidator(0)],required=True)
