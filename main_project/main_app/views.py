from types import MethodType
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from main_app.models import Student

# Create your views here.

def index(request, rollno):
    if Student.objects.filter(rollno=rollno).exists():
        details = Student.objects.get(rollno=rollno)
        attendance= "%.2f" %(float(details.att_classes/details.total_classes)*100)
        telugu_total=details.telugu_mid_marks+details.telugu_final_marks
        hindi_total=details.hindi_mid_marks+details.hindi_final_marks
        english_total=details.english_mid_marks+details.english_final_marks
        maths_total=details.maths_mid_marks+details.maths_final_marks
        science_total=details.science_mid_marks+details.science_final_marks
        social_total=details.social_mid_marks+details.social_final_marks
        total = (telugu_total + hindi_total + english_total + maths_total + science_total + social_total)
        percentage = "%.2f" %(float(total/600)*100)
        return render(request, 'index.html', {'details':details, 'attendance':attendance, 'total':total, 'percentage':percentage, 'telugu_total':telugu_total, 'hindi_total':hindi_total, 'english_total':english_total,'maths_total':maths_total,'science_total':science_total,'social_total':social_total})
    else:
        messages.info(request,'Student Does not Exists')
        return redirect('home')

def home(request):
    return render(request, 'login.html')

def login(request):
    rollno = request.POST['loginid']
    return index(request, rollno)

def logout(request):
    return redirect('/')