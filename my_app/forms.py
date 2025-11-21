from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" #["name","email"]
        # exclude = doj


class ProdctForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        
