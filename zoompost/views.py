from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from .models import GuestModel
import csv


def registerview(request, date):
    form=RegisterForm()
    if request.method=='POST':
        model=GuestModel()
        model.name=request.POST['name']
        model.age = request.POST['age']
        model.gender = request.POST['gender']
        model.university = request.POST['university']
        model.email = request.POST['email']
        model.event_date = request.POST['event_date']

        with open('C:/Users/ioio4/Documents/member_{}.csv'.format(request.POST['event_date']), mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([
                request.POST['name'],
                request.POST['gender'],
                request.POST['email'],
                request.POST['age'],
                request.POST['university']
                ])
        f.close()
            
        model.save()

        return render(request, 'interval.html')

    else:
        event_date=date
        return render(request, 'register.html',{'date':event_date})


def homeview(request):

    return render(request,'index.html')

def intervalview(request):
    return render(request, 'interval.html')


