from django import forms
from .models import Choice

class VoteForm(forms.Form):
    class Meta:
        model = Choice
        voter = forms.CharField(max_length=50)
        comment = forms.CharField(widget=forms.Textarea, required=False)
        fields = ['name', 'choice_text']
    
