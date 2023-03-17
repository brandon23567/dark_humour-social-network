from django.shortcuts import render, redirect
from .models import UploadText, UploadImage
from .forms import UploadTextForm, UploadImageForm

def home(request):
	jokes = UploadText.objects.all().order_by("-date_posted")
	context = {
		'jokes':jokes
	}
	return render(request, "humor/home.html", context)


def say_something(request):
	text_form = UploadTextForm()

	if request.method == "POST":
		text_form = UploadTextForm(request.POST)
		if text_form.is_valid():
			text_form.save()
			return redirect("home")

	context = {
		'text_form':text_form
	}

	return render(request, "humor/say_something.html", context)


def upload_image(request):
	image_form = UploadImageForm()

	if request.method == "POST":
		image_form = UploadImageForm(request.POST, files=request.FILES)
		if image_form.is_valid():
			image_form.save()
			return redirect("crazy_pics")

	context = {
		'image_form':image_form
	}
	
	return render(request, "humor/upload_image.html", context)


def crazy_pics(request):
	images = UploadImage.objects.all().order_by("-date_posted")

	context = {
		'images':images
	}

	return render(request, "humor/crazy_pics.html", context)