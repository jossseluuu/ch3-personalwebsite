from django.http import HttpResponse
from django.shortcuts import render

def homePage_view(request):
      return HttpResponse("Homepage")

def aboutPage_view(request):
      context = {
            "name": "Jose Luis",
            "age" : "20"
      }
      return render(request, "pages/about.html", context)