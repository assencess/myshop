from django import forms

class EmailContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    comments = forms.CharField(required=True, widget=forms.Textarea)

