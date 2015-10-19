from django import forms
from django import *

class VoteForm(forms.ModelForm):
  class Meta:
    model = Vote
    exclude = ('user',)