from django.shortcuts import render, redirect, HttpResponse
from Admin.models import ArchDesRegisterDB
from Employee.models import addPlansDB
from Employee.models import addDesignsDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required


# Create your views here.

def architectHome(req):
    return render(req, 'architectHome.html')


def designerHome(req):
    return render(req, 'designerHome.html')

# @login_required
def addPlan(request):
    # Get the logged in user's id from the session
    user_id = request.session.get('user_id')

    # Query the ArcDesRegisterDB model to get the user's username
    user = ArchDesRegisterDB.objects.filter(pk=user_id).first()
    if user is not None:
        username = user.username
    else:
        username = ''

    # You can then use the `username` variable in your template to set the value of the `Architect` field in your form
    return render(request, 'addPlans.html', {'username': username})

def addDesign(req):
    user1_id = req.session.get('user1_id')

    # Query the ArcDesRegisterDB model to get the user's username
    user = ArchDesRegisterDB.objects.filter(pk=user1_id).first()
    if user is not None:
        username = user.username
    else:
        username = ''

    # You can then use the `username` variable in your template to set the value of the `Architect` field in your form
    return render(req, 'addDesigns.html', {'username': username})


def employeeLogin(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = ArchDesRegisterDB.objects.filter(username=username, password=password, role='Architect', status=1).first()
        user1 = ArchDesRegisterDB.objects.filter(username=username, password=password, role='Designer', status=1).first()
        if user is not None:
            req.session['user_id'] = user.id
            req.session['username'] = user.username
            return render(req, 'architectHome.html')
        elif user1 is not None:
            req.session['user1_id'] = user1.id
            req.session['username1'] = user1.username
            return render(req, 'designerhome.html')       
        else:
            return render(req, 'workwithusADlogin.html', {'error': 'invalid username or password'})
    else:
        return render(req, 'workwithusADlogin.html')


def viewAplans(req):
    user_id = req.session.get('username')
    data = addPlansDB.objects.filter(architect=user_id)
    return render(req, 'viewPlans.html', {'data': data})


def viewDplans(req):
    user_id = req.session.get('username1')
    data = addDesignsDB.objects.filter(designer=user_id)
    return render(req, 'viewDesigns.html', {'data': data})


def savePlan(req):
    if req.method == 'POST':
        plan = req.POST.get('plan')
        squarefeet = req.POST.get('squarefeet')
        numberbedrooms = req.POST.get('numberbedrooms')
        numberbathrooms = req.POST.get('numberbathrooms')
        price = req.POST.get('price')
        description = req.POST.get('description')
        image = req.FILES['image']
        architect = req.POST.get('architect')
        obj = addPlansDB(plan=plan, squarefeet=squarefeet, numberbedrooms=numberbedrooms, numberbathrooms=numberbathrooms, price=price, description=description, image=image, architect=architect)
        obj.save()
        return redirect(architectHome)


def saveDesign(req):
    if req.method == 'POST':
        type = req.POST.get('type')
        style = req.POST.get('style')
        area = req.POST.get('area')
        material = req.POST.get('material')
        price = req.POST.get('price')
        description = req.POST.get('description')
        image = req.FILES['image']
        designer = req.POST.get('designer')
        obj = addDesignsDB(type=type, style=style, area=area, material=material, price=price, description=description, image=image, designer=designer)
        obj.save()
        return redirect(designerHome)


def editPlan(req, plan_id):
    plan = addPlansDB.objects.get(pk=plan_id)
    return render(req, 'editPlan.html', {'plan': plan})


def updatePlan(req, plan_id):
    if req.method == 'POST':
        plan = req.POST.get('plan')
        squarefeet = req.POST.get('squarefeet')
        numberbedrooms = req.POST.get('numberbedrooms')
        numberbathrooms = req.POST.get('numberbathrooms')
        price = req.POST.get('price')
        description = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addPlansDB.objects.get(pk=plan_id).image
        architect = req.POST.get('architect')
        plan1 = addPlansDB.objects.get(pk=plan_id)
        plan1.plan = plan
        plan1.squarefeet = squarefeet
        plan1.numberbedrooms = numberbedrooms
        plan1.numberbathrooms = numberbathrooms
        plan1.price = price
        plan1.description = description
        plan1.image = file
        plan1.architect = architect
        plan1.save()
        return redirect(viewAplans)


def editDesign(req, design_id):
    design = addDesignsDB.objects.get(pk=design_id)
    return render(req, 'editDesign.html', {'design': design})


def updateDesign(req, design_id):
    if req.method == 'POST':
        type = req.POST.get('type')
        style = req.POST.get('style')
        area = req.POST.get('area')
        material = req.POST.get('material')
        price = req.POST.get('price')
        description = req.POST.get('description')
        designer = req.POST.get('designer')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addDesignsDB.objects.get(pk=design_id).image
        design1 = addDesignsDB.objects.get(pk=design_id)
        design1.type = type
        design1.style = style
        design1.area = area
        design1.material = material
        design1.price = price
        design1.description = description
        design1.designer = designer
        design1.image = file
        design1.save()
        return redirect(viewDplans)


def deletePlan(req, plan_id):
    plan1 = addPlansDB.objects.get(pk=plan_id)
    plan1.delete()
    return redirect(viewAplans)


def deleteDesign(req, design_id):
    design1 = addDesignsDB.objects.get(pk=design_id)
    design1.delete()
    return redirect(viewDplans)