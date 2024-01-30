from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

# Create your views here.

def registerpage(request):
    return render(request, "registration.html")

def registerdata(request):
    var_name = request.GET['fn']
    var_email = request.GET['neetu']
    var_contact = request.GET['neha']
    var_password = request.GET['mewada']
    var_con_password = request.GET['kamil']

    Registration.objects.create(
        name = var_name,
        email = var_email,
        contact = var_contact,
        password = var_password,
        co_pass = var_con_password
    )
    return HttpResponse("Done")