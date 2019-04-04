from django import forms

class SuggestionForm(forms.Form):
    suggestion_field = forms.CharField(label='Suggestion', max_length=240)
