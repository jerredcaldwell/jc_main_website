from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class HomePage(TemplateView):
    template_name = 'index.html'

class CareerPage(TemplateView):
    template_name = 'career.html'

class StilesPage(TemplateView):
    template_name = 'stiles.html'

class ClassyPage(TemplateView):
    template_name = 'classy.html'

class Five_StarPage(TemplateView):
    template_name = 'five_star.html'

class MfgPage(TemplateView):
    template_name = '4j_mfg.html'

class EducationPage(TemplateView):
    template_name = 'education.html'

class HobbiesPage(TemplateView):
    template_name = 'hobbies.html'

class HuntingPage(TemplateView):
    template_name = 'hunting.html'

class FishingPage(TemplateView):
    template_name = 'fishing.html'

class AutomotivePage(TemplateView):
    template_name = 'automotive.html'

class ElectronicsPage(TemplateView):
    template_name = 'electronics.html'

class PhotographyPage(TemplateView):
    template_name = 'photography.html'

class VolunteerPage(TemplateView):
    template_name = 'volunteer.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

class LoginPage(TemplateView):
    template_name = 'login.html'
