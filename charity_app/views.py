from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    slider_objects = Slider.objects.all()
    aboutus = Homeaboutus.objects.first()
    event_all = Event.objects.all()
    founder_all = Founder.objects.all()
    donate_all = Donatesection.objects.all()[:6]
    gallery = Gallery.objects.all()[:5]
    faq = Faq.objects.all()[:4]

    blogs = Blog.objects.all()[::-1]
    blogs = blogs[:3]

    brand = Brand.objects.all()

    context = {
        'slider_objects': slider_objects,
        'aboutus':aboutus,
        'event_all':event_all,
        'founder_all':founder_all,
        'donate_all':donate_all,
        'gallery':gallery,
        'faq':faq,
        'blogs':blogs,
        'brand':brand,
    }
    return render(request, 'index.html', context)

def about(request):
    volunteers = Becomeavolunteer.objects.all()
    founders = Founder.objects.all()
    aboutus = Aboutus.objects.first()
    faq = Faq.objects.all()[:4]

    context = {
        'volunteers': volunteers,
        'founders':founders,
        'aboutus':aboutus,
        'faq':faq,
    }
    return render(request, 'subpage/aboutus.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        user = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        user.save()
        
    return render(request, 'subpage/contact.html')

def mainfounder(request):
    mainfounder = Mainfounder.objects.first()
    context = {
        'mainfounder': mainfounder,
    }
    return render(request, 'subpage/about-the-founder.html',context)

def eventdetails(request, slug):
    events = Event.objects.get(slug=slug)
    events_especific = events
    events_photo = EventImage.objects.filter(event=events_especific)
    context = {
        'events':events,
        'events_photo':events_photo,
    }
    return render(request, 'subpage/event-details.html',context)

def eventregistration(request, slug):
    events = Event.objects.get(slug=slug)
    if request.method == 'POST':
        eventid = request.POST.get('eventid')
        eventname = request.POST.get('eventname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        registationtype = request.POST.get('registationtype')

        user = Eventregistation(eventid=eventid, eventname=eventname, name=name, email=email, phone=phone, registationtype=registationtype)
        user.save()

    context = {
        'events':events,
    }
    return render(request, 'subpage/event-registration.html',context)


def donatesection(request, slug):
    donate_details = Donatesection.objects.get(slug=slug)
    print(donate_details)
    context = {
        'donate_details':donate_details,
    }
    return render(request, 'subpage/donation-details.html',context)

def glance(request):
    glance_details = Glance.objects.first()
    context = {
        'glance_details':glance_details,
    }
    return render(request, 'subpage/glance.html',context)

def partnersnetworks(request):
    partners_networks = Partnersnetworks.objects.first()
    context = {
        'partners_networks':partners_networks,
    }
    return render(request, 'subpage/partnersnetworks.html',context)

def awardsrecognation(request):
    awards_recognation = Awardsrecognation.objects.first()
    context = {
        'awards_recognation':awards_recognation,
    }
    return render(request, 'subpage/awards_recognation.html',context)

def donate(request):
    donate_details = Donate.objects.first()
    context = {
        'donate_details':donate_details,
    }
    return render(request, 'subpage/donate.html',context)

def bloglist(request):
    blogs = Blog.objects.all()[::-1]
    context = {
        'blogs':blogs,
    }
    return render(request, 'subpage/blog-list.html',context)

def blogdetails(request, pk):
    blogs = Blog.objects.get(pk=pk)
    categories = Categories.objects.all()

    comment_all = Comment.objects.filter(blog_id=pk)

    all_blogs = Blog.objects.all()

    related_blog_list = []
    for blog in all_blogs:
        if blogs.categories == blog.categories:
            related_blog_list.append(blog)

    if request.method == 'POST':
        blog_id = request.POST.get('blogsId')
        blog = request.POST.get('blog')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        user = Comment(blog_id=blog_id, blog=blog, name=name, email=email, comment=message)
        user.save()


    context = {
        'blogs':blogs,
        'categories':categories,
        'comment_all':comment_all,
        'related_blog_list':related_blog_list,
    }
    return render(request, 'subpage/blog-details.html',context)

def gallerylist(request):
    all_gallery = Gallery.objects.all()
    context = {
        'all_gallery':all_gallery,
    }
    return render(request, 'subpage/gallery-list.html',context)

def socialdevelopment(request):
    social_development_all = Donatesection.objects.all()
    context = {
        'social_development_all':social_development_all,
    }
    return render(request, 'subpage/social-development.html',context)

def becomeavolunteer(request):
    if request.method == 'POST':
        volunteerid = request.POST.get('volunteerid')
        name = request.POST.get('name')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        area = request.POST.get('area')
        reference = request.POST.get('reference')
        equalification = request.POST.get('equalification')
        preaddress = request.POST.get('preaddress')
        paraddress = request.POST.get('paraddress')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        date = request.POST.get('date')
        institute = request.POST.get('institute')
        occupation = request.POST.get('occupation')
        message = request.POST.get('message')

        user = Becomeavolunteer(volunteerid=volunteerid, name=name, image=image, email=email, phone=phone, area=area, reference=reference, equalification=equalification, preaddress=preaddress, paraddress=paraddress, fathername=fathername, mothername=mothername, date=date, institute=institute, occupation=occupation, message=message)
        user.save()

    return render(request, 'subpage/become-volunteer.html')

def sendgift(request):
    sendgift = Sendgift.objects.first()
    context = {
        'sendgift':sendgift,
    }
    return render(request, 'subpage/sendgift.html',context)

def founder(request, pk):
    founders = Founder.objects.get(pk=pk)
    context = {
        'founders':founders,
    }
    return render(request, 'subpage/founder.html',context)

def aboutmore(request):
    about = About.objects.first()
    context = {
        'about':about,
    }
    return render(request, 'subpage/about.html',context)

def notice(request):
    notice_all = Notice.objects.all()
    context = {
        'notice_all':notice_all,
    }
    return render(request, 'subpage/notice.html',context)


    




