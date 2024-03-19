from django.test import TestCase
from django.urls import reverse
from .models import *


# Create your tests here.
# class HomeTestCase(TestCase):
#     def test_home(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index-infotechno.html')
#
#
# class IndexTestCase(TestCase):
#     def test_index(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index-infotechno.html')


class ContactUsTestCase(TestCase):
    def test_contact_us(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact-us.html')


class ServicesTestCase(TestCase):
    def test_services(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'it-services.html')


class ServiceDetailsTestCase(TestCase):
    def test_service_details(self):
        response = self.client.get(reverse('service_details'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'it-services-details.html')


class CareersTestCase(TestCase):
    def test_careers(self):
        response = self.client.get(reverse('careers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers.html')


class LeadershipTestCase(TestCase):
    def test_leadership(self):
        response = self.client.get(reverse('leadership'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leadership.html')


class AboutUsTestCase(TestCase):
    def test_about_us(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-us-01.html')
        
class WhyChooseUsTestCase(TestCase):        
    def test_why_choose_us(self):
        response = self.client.get(reverse('why_choose_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'why-choose-us.html')
        
class TestimonialSectionTestCase(TestCase):        
    def test_testimonial_section(self):
        response = self.client.get(reverse('testimonial_section'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'element-testimonials.html')