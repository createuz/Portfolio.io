from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('resume/', views.resume, name='resume'),
    path('portfolio-detail/', views.portfolio_details, name='portfolio-detail'),
    # path('contact-form/', views.ContactFormView.as_view(), name='contact-form'),

]
