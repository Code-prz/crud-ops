from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import PetReport
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'app/home.html' 

class AboutPageView(TemplateView):
    template_name = 'app/about.html' 


class ContactPageView(TemplateView):
    template_name = 'app/contact.html' 

class DashboardTableListView(ListView):
    template_name = 'app/dashboard_table.html'
    model = PetReport
    context_object_name = 'pet_reports'


class LogPageView(TemplateView):
    template_name = 'app/login.html' 


class PetReportDetailView(DetailView):
    model = PetReport
    template_name = 'app/detail_report.html'
    context_object_name = 'pet_report' 
    success_url = reverse_lazy('dashboard') 

class PetReportCreateView(CreateView):
    model = PetReport
    template_name = 'app/create_report.html'
    fields = ['customer_name', 'pet_name', 'pet_type', 'breed', 'color', 'markings', 'status', 'last_seen_location', 'image']
    success_url = reverse_lazy('report')  


class PetReportUpdateView(UpdateView):
    model = PetReport
    template_name = 'app/update_report.html'  
    fields = ['customer_name', 'pet_name', 'pet_type', 'breed', 'color', 'markings', 'status', 'last_seen_location', 'image']
    success_url = reverse_lazy('dashboard')  

class PetReportDeleteView(DeleteView):
    model = PetReport
    template_name = 'app/delete_report.html' 
    success_url = reverse_lazy('dashboard')
