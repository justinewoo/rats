from django import forms

class selectionForm(forms.Form):
    selection = forms.CharField(label="selection", max_length=100)
