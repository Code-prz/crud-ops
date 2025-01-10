from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, DashboardTableListView, LogPageView, PetReportCreateView, PetReportUpdateView, PetReportDeleteView, PetReportDetailView
urlpatterns = [
    

    path('', HomePageView.as_view(), name = 'home'), 
    path('about/', AboutPageView.as_view(), name = 'about'), 
    path('contact/', ContactPageView.as_view(), name = 'contact'), 
    path('create_report/', PetReportCreateView.as_view(), name='create_report'), 
    path('report_detail/<int:pk>/', PetReportDetailView.as_view(), name='detail_report'),
    path('update_report/<int:pk>/', PetReportUpdateView.as_view(), name='update_report'),
    path('delete_report/<int:pk>/', PetReportDeleteView.as_view(), name='delete_report'),
    path('dashboard/', DashboardTableListView.as_view(), name = 'dashboard'), 
    path('login/', LogPageView.as_view(), name = 'login'), 
]