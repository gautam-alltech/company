from django.db import models

# Create your models here.
# ------------------------------- Index Page Start-----------------------------
    
# Models representation for content section
class Slider(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False )
    sub_title = models.TextField(null=True, blank=True)
    img1 = models.FileField(upload_to='gallery', blank=True, null=True)
    img2 = models.FileField(upload_to='gallery', blank=True, null=True)
     
    def __str__(self):
        return f"Slider {self.title}"
    
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
    
# Models representation for brand section
class Brands(models.Model):
    logo = models.FileField(upload_to='gallery', blank=True, null=True)
    logo_hover = models.FileField(upload_to='gallery', blank=True, null=True)
    
    def __str__(self):
        return f"Brands {self.id}"
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
    
# Models representation for our service section    
class BoxIcon(models.Model):
    box_icon = models.FileField(upload_to='gallery', blank=True, null=True)
    box_heading = models.CharField(max_length=200, null=False, blank=False )
    box_text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Box_Icon {self.box_heading}"
    
    class Meta:
        verbose_name = "Box Icon"
        verbose_name_plural = "Box Icons"

# Models representation for our company section   
class Company(models.Model):
    question_no = models.IntegerField(default=1)
    question = models.CharField(max_length=500, null=False, blank=False)
        
    def __str__(self):
        return f"Company {self.question_no}"
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

# Models representation for hiring section
class LargeBoxImage(models.Model):
    box_icon = models.FileField(upload_to='gallery', blank=True, null=True)
    box_heading = models.CharField(max_length=200, null=False, blank=False )
    box_text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"LargeBoxImage {self.box_heading}"
    
    class Meta:
        verbose_name = "Large Box Image"
        verbose_name_plural = "Large Box Images"

# Models representation for our work section    
class FunFact(models.Model):
    funfact_title = models.CharField(max_length=200, null=False, blank=False )
    funfact_count = models.IntegerField(default = 0)
    funfact_text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"FunFact {self.funfact_title}"
    
    class Meta:
        verbose_name = "Fun Fact"
        verbose_name_plural = "Fun Facts"
        ordering = ['funfact_count']

# Models representation for case studies section   
class Project(models.Model):
    project_img = models.FileField(upload_to='gallery', blank=True, null=True)
    project_heading = models.CharField(max_length=200, null=False, blank=False )
    project_category = models.CharField(max_length=200, null=False, blank=False )
    project_text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Project {self.project_heading}"
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
 
# Models representation for testimonial section   
class Testimonial(models.Model):
    subject = models.CharField(max_length=200, null=False, blank=False )
    text = models.TextField(null=True, blank=True)
    img = models.FileField(upload_to='gallery', blank=True, null=True)
    name = models.CharField(max_length=200, null=False, blank=False )
    post = models.CharField(max_length=200, null=False, blank=False )
    
    def __str__(self):
        return f"Testimonial {self.subject}"
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

#---------------------------------------- Index Page End ---------------------------------

# --------------------------------------- ContactUs Page Start ----------------------------

# Models representation for contactus page
class ContactUs(models.Model):
    location = models.CharField(max_length = 100, null=False, blank=False)
    address = models.CharField(max_length = 200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False, default="+91 0000000000")
    
    def __str__(self):
        return f"Contact {self.location}"
    
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us-s"

#---------------------------------------- ContactUs Page End ---------------------------

#---------------------------------------- Service Page Start ---------------------------

# Models representation for service page   
class Service(models.Model):
    img = models.FileField(upload_to='gallery', blank=True, null=True)
    heading = models.CharField(max_length = 100, null=False, blank=False)
    text = models.CharField(max_length = 200, null=False, blank=False)
    
    def __str__(self):
        return f"Service {self.heading}"
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

#Models representation for advice section
class Advice(models.Model):
    img = models.FileField(upload_to='gallery', blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=1.0)
    text = models.CharField(max_length=100, null=False, blank=False)
    phone_heading = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False, default="+91 0000000000")
    email_heading = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self):
        return f"Advice {self.text}"
    
    class Meta:
        verbose_name = "Advice"
        verbose_name_plural = "Advices"
    
#---------------------------------------- Service Page End ---------------------------

#---------------------------------------- Service details Page Start ---------------------------
#Models representation for banner section
class Banner(models.Model):
    img = models.FileField(upload_to='gallery', blank=True, null=True)
    heading = models.CharField(max_length=100, null=False, blank=False)
    sub_heading = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Banner {self.heading}"
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
    
#Models representation for success story section
class Success(models.Model):
    story = models.CharField(max_length=100, null=False, blank=False)
    text = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return f"Success {self.story}"
    
    class Meta:
        verbose_name = 'Success'
        verbose_name_plural = 'Success-s'
    
#Models representation for security services section
class Security(models.Model):
    service = models.CharField(max_length=100, null=False, blank=False)
    text = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return f"Security {self.service}"
    
    class Meta:
        verbose_name = 'Security'
        verbose_name_plural = 'Securities'
    
#Models representation for monthly pricing table section
class Monthly_Price(models.Model):
    plan_name = models.CharField(max_length=100, null=False, blank=False)
    plan_img = models.FileField(upload_to='gallery', blank=True, null=True)
    plan_currency = models.CharField(max_length=20, null=False, blank=False, default='$')
    plan_price = models.CharField(max_length=10, null=False, blank=False)
    plan_period = models.CharField(max_length=50, null=False, blank=False)
    plan_list_item1 = models.CharField(max_length=100, null=False, blank=False)
    plan_list_item2 = models.CharField(max_length=100, null=False, blank=False)
    plan_list_item3 = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Security {self.plan_name}"
    
    class Meta:
        verbose_name = 'Monthly_Price'
        verbose_name_plural = 'Monthly_Prices'

#Models representation for yearly pricing table section    
class Yearly_Price(models.Model):
    plan_name = models.CharField(max_length=100, null=False, blank=False)
    plan_img = models.FileField(upload_to='gallery', blank=True, null=True)
    plan_currency = models.CharField(max_length=20, null=False, blank=False, default='$')
    plan_price = models.CharField(max_length=10, null=False, blank=False)
    plan_period = models.CharField(max_length=50, null=False, blank=False)
    plan_list_item1 = models.CharField(max_length=100, null=False, blank=False)
    plan_list_item2 = models.CharField(max_length=100, null=False, blank=False)
    plan_list_item3 = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Security {self.plan_name}"
    
    class Meta:
        verbose_name = 'Yearly_Price'
        verbose_name_plural = 'Yearly_Prices'

#------------------------------------Careers Page Start-------------------------------

#Models representation for jobs section
class Jobs(models.Model):
    job_name = models.CharField(max_length=100, null=False, blank=False)
    job_time = models.CharField(max_length=100, null=False, blank=False)
    job_desc = models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return f"Jobs {self.job_name}"
    
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        
#Models representation for gallery section
class Gallery(models.Model):
    img = models.FileField(upload_to='gallery', null=True, blank=True)
    
    def __str__(self):
        return f"Gallery {self.id}"
    
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        
#-------------------------------- Careers Page End ---------------------------------

# ------------------------------- Leadership Page Start ----------------------------

#Models representation for team member section
class TopMember(models.Model):
    image = models.FileField(upload_to='gallery', null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    position = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"TopMember {self.name}"
    
    class Meta:
        verbose_name = 'TopMember'
        verbose_name_plural = 'TopMembers'

#Models representation for team member section
class DownMember(models.Model):
    image = models.FileField(upload_to='gallery', null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    position = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"DownMember {self.name}"
    
    class Meta:
        verbose_name = 'DownMember'
        verbose_name_plural = 'DownMembers'
        
#Models representation for member list section
class MemberList(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    member1 = models.CharField(max_length=100, null=False, blank=False)
    member2 = models.CharField(max_length=100, null=False, blank=False)
    member3 = models.CharField(max_length=100, null=False, blank=False)
    member4 = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"MemberList {self.title}"
    
    class Meta:
        verbose_name = 'MemberList'
        verbose_name_plural = 'MemberLists'
        
#--------------------------------------- Leadership Page End -------------------------