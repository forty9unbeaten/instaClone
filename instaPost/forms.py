from django import forms


class PostForm(forms.Form):
    picture = forms.ImageField()
    caption = forms.CharField(max_length=140, widget=forms.Textarea)