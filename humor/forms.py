from django import forms
from django.forms import ModelForm
from .models import UploadText, UploadImage

class UploadTextForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={"class": "name_input", "placeholder": "Please enter your name, it won't be displayed"}))
	humor = forms.CharField(widget=forms.Textarea(attrs={"class": "humor_input", "placeholder": "Please type in the joke here. Make sure that it it actually funny or don't post at all"}))
	class Meta:
		model = UploadText
		fields = "__all__"

class UploadImageForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={"class": "title_input", "placeholder": "Give your image a title"}))
	caption = forms.CharField(widget=forms.TextInput(attrs={"class": "caption_input", "placeholder": "Give your image a caption unless it doesn't need one?"}))
	class Meta:
		model = UploadImage
		fields = "__all__"