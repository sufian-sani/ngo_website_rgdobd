from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Slider)
admin.site.register(Homeaboutus)

admin.site.register(category)

class EventImages(admin.StackedInline):
    model = EventImage
 
@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    inlines = [EventImages]
 
    class Meta:
       model = Event


admin.site.register(Founder)

admin.site.register(Criteria)
admin.site.register(Donatesection)

admin.site.register(Glance)
admin.site.register(Partnersnetworks)
admin.site.register(Awardsrecognation)

admin.site.register(Donate)

admin.site.register(Mainfounder)
admin.site.register(Gallery)

admin.site.register(Faq)

admin.site.register(Categories)
admin.site.register(Blog)

admin.site.register(Comment)
admin.site.register(Becomeavolunteer)

admin.site.register(Eventregistation)

admin.site.register(Sendgift)

admin.site.register(Brand)

admin.site.register(About)

admin.site.register(Aboutus)

admin.site.register(Contact)
admin.site.register(Notice)
