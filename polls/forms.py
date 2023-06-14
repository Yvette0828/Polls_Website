from django import forms
from .models import PollOption, Choice

class VoteForm(forms.Form):
    class Meta:
        model = Choice
        voter = forms.CharField(max_length=50)
        option = forms.ModelChoiceField(queryset=PollOption.objects.all())
        comment = forms.CharField(widget=forms.Textarea, required=False)
        fields = ['name', 'choice_text']
    
