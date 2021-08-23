from django import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'comptes/profile.html'  

