from django.shortcuts import render, redirect
from Employee.models import addDesignsDB, addPlansDB
from Home.models import customerRegisterDB
# Create your views here.

def homepage(req):
    return render(req, 'homepage.html')

def A(req):
    plans = addPlansDB.objects.all()
    return render(req, 'A.html', {'plans': plans})

def D(req):
    designs = addDesignsDB.objects.all()
    return render(req, 'D.html', {'designs': designs})

def customerRLpage(req):
    return render(req, 'customerRL.html')

def customerSaveData(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm = req.POST.get('confirm')
        if password==confirm:
            obj = customerRegisterDB(name=name, email=email, password=password, confirm=confirm)
            obj.save()
            return redirect(homepage)
    else:
        return render(req, 'customerRL.html', {'msg': 'Password Doesnt Match'})


def customerLogin(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        customer = customerRegisterDB.objects.filter(email=email, password=password).first()
        if customer is not None:
            req.session['name'] = customer.name
            return render(req, 'customerHome.html')
        else:
            return render(req, 'customerRL.html', {'error': 'Invalid Credentials'})

