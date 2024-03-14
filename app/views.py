# from typing import Any
from typing import Any
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView

# Create your views here.

class Home(TemplateView):
    template_name = 'index-infotechno.html'

class Index(TemplateView):
    template_name = 'index-infotechno.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider = Slider.objects.first()
        brands = Brands.objects.all()
        box = BoxIcon.objects.all()
        company = Company.objects.all()
        largebox = LargeBoxImage.objects.all()
        funfact = FunFact.objects.all()
        projects = Project.objects.all()
        testimonial = Testimonial.objects.all()
        context.update({
            'slider': slider,
            'brands': brands,
            'box': box,
            'company': company,
            'largebox': largebox,
            'funfact': funfact,
            'projects': projects,
            'testimonial': testimonial,
        })
        return context

class ContactUs(TemplateView):
    model = ContactUs
    template_name = 'contact-us.html'
    context_object_name = 'contact'

class Services(TemplateView):
    template_name = 'it-services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.all()
        advice = Advice.objects.first()
        context.update({
            'services': services,
            'advice': advice,
        })
        return context

class ServiceDetails(TemplateView):
    template_name = 'it-services-details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banner = Banner.objects.first()
        success = Success.objects.all()
        security = Security.objects.all()
        monthly_price = Monthly_Price.objects.all()
        yearly_price = Yearly_Price.objects.all()
        context.update({
            'banner':banner,
            'success':success,
            'security':security,
            'monthly_price':monthly_price,
            'yearly_price':yearly_price
        })
        return context

class Careers(TemplateView):
    template_name = 'careers.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = Jobs.objects.all()
        gallery = Gallery.objects.all()
        context.update({
            'jobs':jobs,
            'gallery':gallery
        })
        return context
    
class Leadership(TemplateView):
    template_name = 'leadership.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topmember = TopMember.objects.all()
        downmember = DownMember.objects.all()
        memberlist = MemberList.objects.all()
        context.update({
            'topmember':topmember,
            'downmember':downmember,
            'memberlist':memberlist
        })
        return context