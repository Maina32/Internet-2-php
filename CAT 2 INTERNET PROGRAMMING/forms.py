from django import forms
from .models import Obituary
from django.core.validators import MinLengthValidator

class ObituaryForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        validators=[MinLengthValidator(50)]
    )
    
    class Meta:
        model = Obituary
        fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_death': forms.DateInput(attrs={'type': 'date'}),
        }