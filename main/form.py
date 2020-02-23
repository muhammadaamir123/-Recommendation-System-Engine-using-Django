from django import forms

class Form(forms.Form):
	search = forms.CharField()