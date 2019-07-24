from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# look up args and kwargs
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})