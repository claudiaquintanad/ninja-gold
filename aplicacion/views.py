from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    return render(request,'index.html')

def processmoney(request):
    if 'contador' in request.session:
        if request.POST['ninja'] == 'Farm': 
            earn = random.randint(10,20)
            request.session['contador'] += earn
            request.session['salida'].append({'text': f"Earned {earn} golds from the casino!"})
            request.session.save()
        if request.POST['ninja'] == 'Cave': 
            earn = random.randint(5,10)
            request.session['contador'] += earn
            request.session['salida'].append({'text': f"Earned {earn} golds from the casino!"})
            request.session.save()
        if request.POST['ninja'] == 'House': 
            earn = random.randint(2,5)
            request.session['contador'] += earn
            request.session['salida'].append({'text': f"Earned {earn} golds from the casino!"})
            request.session.save()
        if request.POST['ninja'] == 'Casino': 
            earn = random.randint(-50,50)
            request.session['contador'] += earn
            if earn > 0:
                request.session['salida'].append({'text': f"Earned {earn} golds from the casino!"})
                request.session.save()
            else:
                request.session['salida'].append({'text': f"Entered a casino and lost {earn} golds...Ouch..."})
                request.session.save()

    else:
        request.session['contador'] = 0
        request.session['salida'] = []
    return redirect("/")

def reset(request):
    if request.method == "POST":
        request.session['contador'] = 0
        request.session['salida'] = []
    return redirect('/')