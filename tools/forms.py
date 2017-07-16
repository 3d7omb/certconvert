from django import forms

class UploadForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    file = forms.FileField()
