"""MiTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import *
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('index/', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services.as_view(), name='services'),
    path('service_details/', ServiceDetails.as_view(), name='service_details'),
    path('careers/', Careers.as_view(), name='careers'),
    path('leadership/', Leadership.as_view(), name='leadership'),
    path('about_us/', AboutUs.as_view(), name='about_us'),
    path('why_choose_us/', WhyChooseUs.as_view(), name='why_choose_us'),
    path('testimonial_section/', TestimonialSection.as_view(), name='testimonial_section'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
