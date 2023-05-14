"""tbh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('mainapp.urls', namespace='mainapp')),
    path('', views.HomePage.as_view(),name='home'),
    path('career/',views.CareerPage.as_view(),name='career'),
    path('stiles/',views.StilesPage.as_view(),name='stiles'),
    path('classy/',views.ClassyPage.as_view(),name='classy'),
    path('five_star/',views.Five_StarPage.as_view(),name='five_star'),
    path('mfg/',views.MfgPage.as_view(),name='mfg'),
    path('education/',views.EducationPage.as_view(),name='education'),
    path('hobbies/',views.HobbiesPage.as_view(),name='hobbies'),
    path('hunting/',views.HuntingPage.as_view(),name='hunting'),
    path('fishing/',views.FishingPage.as_view(),name='fishing'),
    path('automotive/',views.AutomotivePage.as_view(),name='automotive'),
    path('electronics/',views.ElectronicsPage.as_view(),name='electronics'),
    path('photography/',views.PhotographyPage.as_view(),name='photography'),
    path('volunteer/',views.VolunteerPage.as_view(),name='volunteer'),
    path('contact/',views.ContactPage.as_view(),name='contact'),
    path('login/',views.LoginPage.as_view(),name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
