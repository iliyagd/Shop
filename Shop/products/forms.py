from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='search')

class Image(forms.Form):
    Image = forms.ImageField()
    