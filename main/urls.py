from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path("", views.homepage, name="Home"),
	path("about/", views.aboutpage, name="about"),
	path("result/", views.resultpage, name="result"),
	# path("error", views.search, name="errorpage")
]