from django import forms

class ContUsForm(forms.Form):
	name=forms.CharField(label='name', max_length=100)
	message=forms.CharField(label='message', widget=forms.Textarea)