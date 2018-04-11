from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='upload your output file',
    
    )