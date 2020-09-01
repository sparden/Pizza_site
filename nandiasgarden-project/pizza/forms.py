from django import forms
from .models import Pizza,Size
"""class PizzaForm(forms.Form):
     topping1= forms.CharField(label='Topping 1',max_length=200)
     topping2= forms.CharField(label='Topping 2',max_length=200)
     size= forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])"""
     
class PizzaForm(forms.ModelForm):

 #   size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
 #   size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
 #   email = forms.EmailField()
 #   url = forms.URLField()
 #    image =forms.ImageField()//to get image to on your form so that user can upload
	 
     class Meta:
         model =Pizza
         fields =['topping1','topping2','size']  
         labels ={'topping1':'Topping 1','topping2':'Topping 2'} #discnorary datatype we ussed
 #       widgets ={'size':forms.CheckboxSelectMultiple}  

class MultiplePizzaForm(forms.Form):
     number = forms.IntegerField(min_value=2,max_value=6) 