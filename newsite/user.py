from django.shortcuts import render, redirect
from newsite.forms import RegisterForm
from newsite.forms import Addnewsform, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from newsite.models import Addusernews
from django.contrib.auth.decorators import login_required

from requests import session
import requests
# Register new id

def userregister(request):
    form = RegisterForm()

    if request.method == "POST":
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if password != confirmation:
            messages.error(request, "Passwords must match.")

        else:
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            name = request.POST["name"]
            if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email=email)) == 0:
                nyuser = User.objects.create_user(username, email, password)
                nyuser.first_name = name
                nyuser.save()

                return redirect('/')

            else:
                messages.error(request, "user already exist")

    else:
        form = RegisterForm()
        print("this is error no 2: \n", form.errors)

    return render(request, 'CustomerRegister/register.html', {'form': form})

def userlogin(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username != "" and password != "":
            print("abc")
            user = authenticate(username=username, password=password)
            print(user)

            if user != None:
                login(request, user)
                print(request.session['_auth_user_id'])
                print(request.session['_auth_user_backend'])
                print(request.session['_auth_user_hash'])
                messages.info(request, f"you are now logged in as {username}.")
                return redirect("/dashboard")
            else:
               messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please Enter valid Details.You Enter Username or Password is blank")

    form = AuthenticationForm
    return render(request, 'LogInPage/loginpage.html', {'form': form})

def userdashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request, 'LogInPage/dashboard.html')

def useraddnews(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == "POST":
        form = Addnewsform(request.POST)
        if form.is_valid():
            try:
                # form.user_id = 1
                # form.user = request.user
                select_value = request.POST.get('Category')
                #city = form.cleaned_data['city']
                newsform = form.save(commit=False)
                #thought.User = userObj
                newsform.user = request.user
                newsform.save()
                # form.save()
                return redirect("/dashboard")
            except Exception as e: print(e)

        else:
            print("invalid")
            print(form.errors)
            exit()
    else:
        form = Addnewsform()

    return render(request, 'LogInPage/addnews.html', {'form': form})

def mylogout(request):

    logout(request)

    return redirect('/')

def usermynews(request):
    id = request.user.id
    print(id)
    news1 = Addusernews.objects.filter(user_id=id)
    return render(request, 'LogInPage/mynews.html', {'news1':news1})

def edit(request, id):
    news = Addusernews.objects.get(id=id)
    return render(request, 'LogInPage/editnews.html', {'news':news})

@login_required
def update(request, id):
    # news = Addusernews.objects.get(id=id)
    # form = Addnewsform(request.POST, instance = news)
    # if form.is_valid():
    #     form.save()
    #     return redirect("/mynews")
    # else:
    #     print(form.errors)
    #
    # return render(request, 'LogInPage/editnews.html', {'news': news})
    print("all starts here")
    news = Addusernews.objects.get(id=id)
    print(id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            print("it's saved")
            messages.success(request, 'Your profile is updated successfully')
            return redirect("/mynews")
    else:
        form = UpdateUserForm(instance=request.user)
        print("it's not")
        print(form.errors)


    # return render(request, 'users/profile.html', {'user_form': user_form}) // just for example
    return render(request, 'LogInPage/editnews.html', {'news': news, 'form': form})


def destroy(request, id):
    news = Addusernews.objects.get(id=id)
    news.delete()
    return redirect("/mynews")




