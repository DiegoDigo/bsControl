from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def dashbord(request):
    return render(request, "main/deshbord.html",{})