from django import forms

from .models import post

class postform(forms.ModelForm):
	class Meta:
		model = post
		fields = [
			"title",
			"content",
			"image",
			"author",
			"email"
		]