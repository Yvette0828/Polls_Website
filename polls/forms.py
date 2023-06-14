from django import forms
from .models import PollOption

class VoteForm(forms.Form):
    option = forms.ModelChoiceField(queryset=PollOption.objects.all())
    comment = forms.CharField(widget=forms.Textarea, required=False)
