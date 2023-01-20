from django.shortcuts import render, redirect
from Admin.models import ArchDesRegisterDB
from Home.views import homepage
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from Home.views import homepage




# Create your views here.

# -------------------------Admin Different Pages View-----------------------------

def adminHomePage(req):
    return render(req, 'index.html')


def approveArchitect(req):
    architects = ArchDesRegisterDB.objects.filter(role='Architect', status=0)
    if req.method == 'POST':
        pk = req.POST.get('architect_id')
        status = req.POST.get('approval_choice')
        architect = get_object_or_404(ArchDesRegisterDB, pk=pk)
        architect.status = status
        architect.save()
    return render(req, 'approveArchitect.html', {'architects': architects})


def approveDesigner(req):
    designers = ArchDesRegisterDB.objects.filter(role = 'Designer', status=0)
    if req.method == 'POST':
        pk = req.POST.get('designer_id')
        status = req.POST.get('approval_choice')
        designer = get_object_or_404(ArchDesRegisterDB, pk=pk)
        designer.status = status
        designer.save()
    return render(req, 'approveDesigner.html', { 'designers': designers })

def viewData(req, dataid):
    data = ArchDesRegisterDB.objects.filter(id=dataid)
    return render(req, 'viewA.html', {'data': data})

def viewData1(req, dataid):
    data = ArchDesRegisterDB.objects.filter(id=dataid)
    return render(req, 'viewD.html', {'data': data})


def manageArchitect(req):
    architects = ArchDesRegisterDB.objects.filter(role = 'Architect', status = 1)
    return render(req, 'manageArchitect.html', {'architects': architects})


def viewMA(req, dataid):
    data = ArchDesRegisterDB.objects.filter(id=dataid)
    return render(req, 'viewMA.html', {'data': data})


def viewMD(req, dataid):
    data = ArchDesRegisterDB.objects.filter(id=dataid)
    return render(req, 'viewMD.html', {'data': data})



def manageDesigner(req):
    designers = ArchDesRegisterDB.objects.filter(role = 'Designer', status = 1)
    return render(req, 'manageDesigner.html', {'designers': designers})


def workWithUsLogin(req):
    return render(req, 'workwithusADlogin.html')


def workWithUsRegister(req):
    return render(req, 'workwithusADregister.html')


def adminLoginPage(req):
    return render(req, 'adminlogin.html')


def adminSuper(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        if User.objects.filter(username__contains=username).exists():
            user = authenticate(username=username, password=password)

            if user is not None:
                login(req, user)
                req.session['username']=username
                req.session['password']=password
                return redirect(adminHomePage)
            else:
                return redirect(adminLoginPage)
        else:
            return redirect(adminLoginPage)



# -------------------------Admin Different Pages View END-----------------------------


#--------------------------Delete----------------------------------------------

def deleteArchitect(req, dataid):
    data = ArchDesRegisterDB.objects.filter(id=dataid)
    data.delete()
    return redirect(manageArchitect)


def deleteDesigner(req, dataid):
    data = ArchDesRegisterDB.objects.filter(id=dataid)
    data.delete()
    return redirect(manageDesigner)






# -------------------------Delete End------------------------------------------ 


# -------------------------Database Save----------------------------------------------------


def RegisterArchitectDesigner(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        username = req.POST.get('username')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        role = req.POST.get('role')
        experience = req.POST.get('experience')
        image = req.FILES['image']
        if password == confirm_password:
            obj = ArchDesRegisterDB(name=name ,email=email, username=username, password=password, confirm_password=confirm_password, role=role, experience=experience , image=image)
            obj.save()
            return redirect(homepage)
        else:
            return render(req, 'workwithusADregister.html', {'error': 'password does not match'})
        


# -------------------------Database Save end----------------------------------------------------

def LogOut(req):
    return redirect(homepage)


