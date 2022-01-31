from django import forms
from .models import review

class reviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':30}))

    class Meta:
        model= review
        fields = ['review']
        