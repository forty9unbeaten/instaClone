from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=140, widget=forms.Textarea, required=False)
    email = forms.EmailField(max_length=150, required=False)
    url = forms.URLField(required=False)
    