from django.shortcuts import render
from django.http import HttpResponse
from .form import Form
from .scrapper import Scrap
# Create your views here.

def homepage(request):
	text = 'No search query'
	result = 0
	hide = 'hide'
	if request.method == 'POST':
		form = Form(request.POST)

		if form.is_valid():
			text = form.cleaned_data.get('search')
			scrap = Scrap(text)
			result = scrap.scrapeSite()
			return render(request, 'main/home.html', {'positive':result[0],'negative':result[1],'hide':result[2]})

	return render(request, 'main/home.html',{'hide':hide})

def aboutpage(request):
	return render(request, 'main/about.html')
def resultpage(request):
	return render(request, 'main/result.html')
# def search(request):
# 	text = 'No search query'

# 	if request.method == 'POST':
# 		form = Form(request.POST)

# 		if form.is_valid():
# 			text = form.cleaned_data.get('search')
			

# 	return render(request, "main/error.html", {"text":text})