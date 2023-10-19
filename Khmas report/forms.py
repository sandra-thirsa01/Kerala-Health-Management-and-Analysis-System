from django import forms
c= [
    ('pneumonia', 'Pneumonia'),
    ('astma','Astma'),
    ('sephesis', 'Sephesis'),
    ('tetanus','Tetanus'),
    ('tuberculosis','Tuberculosis'),
    ]
c1= [
    ('opv0 ', 'OPV0'),
    ('bcg','BCG'),
    ('hep_B0', 'Hep_B0'),
    ]    
class Dashboards(forms.Form):
    disease=forms.CharField(label='Choose Disease', widget=forms.Select(choices=c))
class CvrDashboard(forms.Form):
    vaccine=forms.CharField(label='Choose Vaccine', widget=forms.Select(choices=c1))    


