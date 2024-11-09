from django import forms
from django.core import validators

class ForName (forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5)])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='input your email again:')
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure your email is match!")
        