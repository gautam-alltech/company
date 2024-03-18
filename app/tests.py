from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class AppTestCase(TestCase):
    def setUp(self):
        self.slider = Slider.objects.create()
        self.brands = Brands.objects.create()
        self.box = BoxIcon.objects.create()
        self.company = Company.objects.create()
        self.largebox = LargeBoxImage.objects.create()
        self.funfact = FunFact.objects.create()
        self.projects = Project.objects.create()
        self.testimonial = Testimonial.objects.create()
        self.contactus = ContactUs.objects.create()
        self.service = Service.objects.create()
        self.advice = Advice.objects.create()
        self.banner = Banner.objects.create()
        self.success = Success.objects.create()
        self.security = Security.objects.create()
        self.monthly_price = Monthly_Price.objects.create()
        self.yearly_price = Yearly_Price.objects.create()
        self.jobs = Jobs.objects.create()
        self.gallery = Gallery.objects.create()
        self.topmember = TopMember.objects.create()
        self.downmember = DownMember.objects.create()
        self.memberlist = MemberList.objects.create()
        self.aboutusstory = AboutUsStory.objects.create()
        self.aboutussolution = AboutUsSolution.objects.create()
        self.aboutusfunfact = AboutUsFunFact.objects.create()
        self.aboutustestimonial = AboutUsTestimonial.objects.create()
        self.aboutusbrand = AboutUsBrand.objects.create()
        
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index-infotechno.html')
        
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index-infotechno.html')
        
    def test_contact_us(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-us.html')
        
    def test_services(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'it-services.html')
        
    def test_service_details(self):
        response = self.client.get(reverse('service_details'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'it-services-details.html')
        
    def test_careers(self):
        response = self.client.get(reverse('careers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers.html')
        
    def test_leadership(self):
        response = self.client.get(reverse('leadership'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leadership.html')
        
    def test_about_us(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-us-01.html')