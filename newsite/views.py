from django.shortcuts import render, redirect
from newsite.forms import EmployeesForm
from newsite.models import Employees
from newsite.forms import RegisterForm
import requests

# Create your views here.
def index(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['data'] = inshorts_data
    return render(request, 'index.html', records)

def international(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=international"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['internationaldata'] = inshorts_data
    return render(request, 'international.html', records)


def health(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=health"
    response = requests.get(url=url)
    # print(response)
    inshorts_data = response.json()
    records['healthdata'] = inshorts_data
    print(records)
    return render(request, 'health.html', records)

def education(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=education"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['educationdata'] = inshorts_data
    return render(request, 'education.html', records)

def sports(request):
    records={}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['sportsdata']=inshorts_data
    return  render(request, 'sports.html', records)

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['entertainmentdata'] = inshorts_data
    return render(request, 'entertainment.html', records)

def politics(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=politics"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['politicsdata'] = inshorts_data
    return render(request, 'politics.html', records)

def technology(request):
    records={}
    url = "https://inshortsapi.vercel.app/news?category=technology"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['technologydata']=inshorts_data
    return render(request, 'technology.html', records)


def startup(request):
    records={}
    url = "https://inshortsapi.vercel.app/news?category=startup"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['startupdata']=inshorts_data
    return render(request, 'startup.html', records)

def science(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=science"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sciencedata'] = inshorts_data
    return render(request, 'science.html', records)

def automobile(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=automobile"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['automobiledata']=inshorts_data
    return render(request, 'automobile.html', records)

def national(request):
    records={}
    url = "https://inshortsapi.vercel.app/news?category=national"
    response=requests.get(url=url)
    inshorts_data=response.json()
    records['nationaldata']=inshorts_data
    return render(request,'national.html',records)

def world(request):
    records={}
    url = "https://inshortsapi.vercel.app/news?category=world"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['worlddata'] = inshorts_data
    return render(request, 'world.html', records)

def miscellaneous(request):
    records={}
    url = "https://inshortsapi.vercel.app/news?category=miscellaneous"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['miscellaneousdata'] = inshorts_data
    return render(request, 'miscellaneous.html', records)

def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['businessdata'] = inshorts_data
    return render(request, 'business.html', records)

def hatke(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=hatke"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['hatkedata'] = inshorts_data
    return render(request, 'hatke.html', records)


# Create Employees view
def emps(request):

    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            print("invalid")
            exit()
    else:
        form = EmployeesForm()
    return render(request, 'indexE.html', {'form': form})

def show(request):
    employee1 = Employees.objects.all()
    return render(request, 'show.html', {'employee1': employee1})

def edit(request, id):
    employee = Employees.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

def update(request, id):
    employee = Employees.objects.get(id=id)
    form = EmployeesForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    else:
        print(form.errors)
    return render(request, 'edit.html', {'employee': employee})

def destroy(request,id):
    employee = Employees.objects.get(id=id)
    employee.delete()
    return redirect("/show")


# Register new id

def userregister(request):

    errorMessage = ""
    if request.method == "POST":
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            errorMessage = "Passwords must match."

        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
        else:
            print("this is error: \n", form.errors)
    else:
        form = RegisterForm()
        print("this is error no 2: \n", form.errors)

    return render(request,'CustomerRegister/register.html', {'form':form, 'message': errorMessage})