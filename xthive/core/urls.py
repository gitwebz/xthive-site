from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('case-studies/<slug:slug>/', views.case_study_detail, name='case_study_detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('pricing/', views.pricing, name='pricing'),
]