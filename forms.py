from django import forms
from .models import text


class mytext(forms.ModelForm):

	# Dairy = forms.CharField(widget=forms.Textarea)
	# Dairy = forms.CharField(widget=forms.Textarea(attrs={"rows": 40, "cols": 100}))

	class Meta:
		model= text
		fields=[
            'Dairy'
		]
