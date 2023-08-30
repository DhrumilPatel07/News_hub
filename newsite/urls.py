from django.urls import path, include
from . import views
from newsite import user





urlpatterns = [
    path('', views.index, name="indexfile"),
    path('international', views.international, name="internationalfile"),
    path('national', views.national, name="nationalfile"),
    path('entertainment', views.entertainment, name="entertainmentfile"),
    path('politics', views.politics, name="politicsfile"),
    path('health', views.health, name="healthfile"),
    path('sports', views.sports, name="sportsfile"),
    path('education', views.education, name="educationfile"),
    path('business', views.business, name="businessfile"),
    path('miscellaneous', views.miscellaneous, name="miscellaneousfile"),
    path('world', views.world, name="worldfile"),
    path('science', views.science, name="sciencefile"),
    path('hatke', views.hatke, name="hatkefile"),
    path('technology', views.technology, name="technologyfile"),
    path('automobile', views.automobile, name="automobilefile"),
    path('startup', views.startup, name="startupfile"),
    path('userregister', user.userregister, name="userregisterfile"),
    path('login', user.userlogin, name="loginfile"),
    path('dashboard', user.userdashboard, name="dashboardfile"),
    path('addnews', user.useraddnews, name="addnewsfile"),
    path('mylogout', user.mylogout, name="mylogout"),
    path('mynews', user.usermynews, name="mynewsfile"),
    path('edit/<int:id>', user.edit),
    path('update/<int:id>', user.update),
    path('delete/<int:id>', user.destroy),
    path("accounts/", include("django.contrib.auth.urls"))

]