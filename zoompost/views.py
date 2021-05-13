from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from .models import GuestModel
import csv
import requests 


def registerview(request, date):
    if request.method=='POST':
        model=GuestModel()
        model.name=request.POST['name']
        model.age = request.POST['age']
        model.gender = request.POST['gender']
        model.university = request.POST['university']
        model.email = request.POST['email']
        model.event_date = request.POST['event_date']
        model.save()    

        api = "https://notify-api.line.me/api/notify"
        token = "0wCPeo8wg56X7caRHcX1ERVR0EFg7GsS0MW8NeyUd7n"
        headers = {"Authorization" : "Bearer "+ token}

        message = "名前：{0}　性別：{1}　年齢：{2}　日程：{3}　人数：{4}".format(
            request.POST['name'],
            request.POST['gender'],
            request.POST['age'],
            request.POST['event_date'],
            request.POST['member']
            )
        payload = {"message" :  message}

        post = requests.post(api, headers = headers, params=payload, files=None)

        with open('/usr/share/nginx/html/static/zoompost/csv/member_{0}_{1}.csv'.format(request.POST['event_date'],request.POST['gender']), mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([
                request.POST['name'],
                request.POST['gender'],
                request.POST['email'],
                request.POST['age'],
                request.POST['university'],
                request.POST['member'],
                "",
                request.POST['friend_name'],
                request.POST['friend_email']
                ])
        f.close()    
        return render(request, 'interval.html')

    else:
        event_date=date
        return render(request, 'register.html',{'date':event_date})


def homeview(request):

    return render(request,'index.html')

def intervalview(request):
    return render(request, 'interval.html')




