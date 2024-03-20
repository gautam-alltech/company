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
        box = BoxIcon.objects.filter(page='box')
        company = Company.objects.all()
        largebox = BoxIcon.objects.filter(page='largebox')
        funfact = FunFact.objects.all()
        projects = Gallery.objects.filter(page='projects')
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
    
class Contact(TemplateView):
    template_name = 'contact-us.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contactus = ContactUs.objects.all()
        context.update({
            'contactus':contactus
        })
        return context

class Services(TemplateView):
    template_name = 'it-services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = BoxIcon.objects.filter(page='services')
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
        success = Success.objects.filter(page='success')
        security = Success.objects.filter(page='security')
        monthly_price = {} # Monthly_Price.objects.all()
        yearly_price = {} # Yearly_Price.objects.all()
        context.update({
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
        gallery = Gallery.objects.filter(page='gallery')
        context.update({
            'jobs':jobs,
            'gallery':gallery
        })
        return context
    
class Leadership(TemplateView):
    template_name = 'leadership.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topmember = {} # TopMember.objects.all()
        downmember = {} # DownMember.objects.all()
        memberlist = MemberList.objects.all()
        context.update({
            'topmember':topmember,
            'downmember':downmember,
            'memberlist':memberlist
        })
        return context
    
class AboutUs(TemplateView):
    template_name = 'about-us-01.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutusstory = BoxIcon.objects.filter(page='aboutusstory')
        aboutussolution = AboutUsSolution.objects.all()
        aboutusfunfact = {} # AboutUsFunFact.objects.all()
        aboutustestimonial = {} #AboutUsTestimonial.objects.all()
        aboutusbrand = {} # AboutUsBrand.objects.all()
        context.update({
            'aboutusstory':aboutusstory,
            'aboutussolution':aboutussolution,
            'aboutusfunfact':aboutusfunfact,
            'aboutustestimonial':aboutustestimonial,
            'aboutusbrand':aboutusbrand
        })
        return context
    
class WhyChooseUs(TemplateView):
    template_name = 'why-choose-us.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        progresschart = ProgressChart.objects.all()
        features = BoxIcon.objects.filter(page='features')
        context.update({
            'progresschart':progresschart,
            'features':features
        })
        return context
    
class TestimonialSection(TemplateView):
    template_name = 'element-testimonials.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # testimonialpage = TestimonialPage.objects.all()
        testimonialpage = {}
        context.update({
            'testimonialpage':testimonialpage
        })
        return context