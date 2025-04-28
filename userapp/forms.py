from django import forms
from.models import Reg_tbl


class Regform(forms.Form):
    Fullname = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Mobilenumber = forms.IntegerField()
    Password = forms.CharField(max_length=20)




# we use modelform class instead of form class when the model or table is exist( we take fields from Reg_tbl)





class Regform(forms.ModelForm):
    class Meta:
        model=Reg_tbl
        fields=("__all__")


#if we only need 2 fields which name and mobile

class Regform(forms.ModelForm):
    class Meta:
        model=Reg_tbl
        fields=['mob','fnm']

class Regform(forms.ModelForm):
    class Meta:
        fields=['fnm','mob','eml','psw','cpsw']
        model=Reg_tbl
        widgets={
            'fnm' : forms.TextInput(attrs={'class':'form-control','placeholder':'full name','border-color':'green'}),
            'mob' : forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'eml' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'psw' : forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}),
            'cpsw' : forms.TextInput(attrs={'class':'form-control','placeholder':'ConfirmPassword'})
            
        }








    