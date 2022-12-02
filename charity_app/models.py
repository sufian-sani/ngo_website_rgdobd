from email.mime import message
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Slider(models.Model):
    subtitle = models.CharField(max_length=500, blank=True,null=True)
    title = models.CharField(max_length=200, blank=True,null=True)
    url_field = models.URLField(blank=True,null=True)
    background_image = models.ImageField(upload_to='slider_image')

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

class Homeaboutus(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='abouthome_image')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Home Aboutus"
        verbose_name_plural = "Home Aboutus"

class category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Category"

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True,blank=True,null=True)
    image = models.ImageField(upload_to='event_image',blank=True,null=True)
    date = models.DateField()
    details = RichTextUploadingField()
    details_optional = RichTextUploadingField(blank=True,null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Event"
        verbose_name_plural = "Event"

class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'event_image/', blank=True, null=True)
 
    def __str__(self):
        return self.event.title

class Eventregistation(models.Model):
    eventid = models.IntegerField()
    eventname = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    registationtype = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Event Registation"
        verbose_name_plural = "Event Registation"


class Founder(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=100)
    image = models.FileField(upload_to = 'founder_image/')
    speech = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Founder"
        verbose_name_plural = "Founder"

class Criteria(models.Model):
    donate_criteria = models.CharField(max_length=300)

    def __str__(self):
        return self.donate_criteria

    class Meta: 
        verbose_name = "Donate Criteria"
        verbose_name_plural = "Donate Criteria"

class Donatesection(models.Model):
    feature_image = models.ImageField(upload_to='donatesection_image')
    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='title', unique=True,blank=True,null=True)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=True,null=True)
    goal_show = models.BooleanField(default=False)
    raised = models.IntegerField(blank=True, null=True)
    goal = models.IntegerField(blank=True, null=True)
    summary = RichTextField(config_name='abasic_ckeditor',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Donate Section"
        verbose_name_plural = "Donate Section"

class Glance(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "At a Glance"
        verbose_name_plural = "At a Glance"

class Partnersnetworks(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Partners & Networks"
        verbose_name_plural = "Partners & Networks"

class Awardsrecognation(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Awards & Recognation"
        verbose_name_plural = "Awards & Recognation"

class Donate(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Donate"
        verbose_name_plural = "Donate"

class Mainfounder(models.Model):
    image = models.ImageField(upload_to='founder')
    name = models.CharField(max_length=500)
    description = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Main Founder"
        verbose_name_plural = "Main Founder"

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=500)

    def __str__(self):
        return self.sub_title

    class Meta: 
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

class Faq(models.Model):
    question = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.question

    class Meta: 
        verbose_name = "Faq"
        verbose_name_plural = "Faq"

class Categories(models.Model):
    categories = models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    class Meta: 
        verbose_name = "Categories"
        verbose_name_plural = "Categories"

class Blog(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=500)
    description = RichTextUploadingField(blank=True,null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

class Comment(models.Model):
    blog_id = models.IntegerField()
    blog = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    comment = models.TextField()
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + "," + "[blog name]: " +self.blog + "," + "[blog ID]: " + str(self.blog_id)

    class Meta: 
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comment"

class Becomeavolunteer(models.Model):
    volunteerid = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='volunteer')
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    area = models.CharField(max_length=200)
    reference = models.CharField(max_length=13)
    equalification = models.CharField(max_length=200)
    preaddress = models.CharField(max_length=200)
    paraddress = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    mothername = models.CharField(max_length=200)
    date = models.CharField(max_length=10)
    institute = models.CharField(max_length=200)
    occupation = models.CharField(max_length=80)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Become a Volunteer"
        verbose_name_plural = "Become a Volunteer"

class Sendgift(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Send a Gift"
        verbose_name_plural = "Send a Gift"

class Brand(models.Model):
    image = models.ImageField(upload_to='brand/')

    class Meta: 
        verbose_name = "Brand"
        verbose_name_plural = "Brand"

class Aboutus(models.Model):
    image_1 = models.ImageField(upload_to='aboutus/')
    image_2 = models.ImageField(upload_to='aboutus/')
    title = models.CharField(max_length=300)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "About"
        verbose_name_plural = "About"



class About(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "About More"
        verbose_name_plural = "About More"

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

class Notice(models.Model):
  title = models.CharField(max_length=500)
  file = models.FileField(upload_to='notice/')
  publish_date = models.DateField(auto_now_add=True)

  def __str__(self):
        return self.title

  class Meta: 
    verbose_name = "Notice"
    verbose_name_plural = "Notice"













