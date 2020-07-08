from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import os
def index(request):
    return render(request,'basic.html')
    # return HttpResponse("Hello")

def submission(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    username = request.GET.get('username')
    dob = request.GET.get('DOB')
    gender = request.GET.get('gender')
    feedback = request.GET.get('feedback')
    dic = {'name':name, 'email':email,'username':username,'gender':gender,'feedback':feedback,'dob':dob}
    print(name,email,username,gender,feedback)
    
    return render(request,'submission.html',dic)