from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import ContactUs
from django.contrib import messages
from .models import (
    Navlogo,
    Navitem_1,
    Navitem_2,
    Navitem_3,
    Navitem_4,
    Navitem_5,
    Navitem_6,
    Navsubitem_1,
    Navsubitem_2,
    Navsubitem_3,
    Navsubitem_4,
    Navsubitem_5,
    Navsubitem_6,
    HomeBg,
    LeftMenu,
    LeftContact,
    Latesttitle,
    LastestPicture,
    ClientLogo,
    WhatWedo,
    Servicetitle,
    Services,
    ServicesBtn,
    Creative,
    ContactU,
    ContactForm,
    Gallery,
    GalleryColumn1image,
    GalleryColumn2image,
    GalleryColumn3image,
    GalleryColumn4image,
    FooterColumn1,
    FooterColumn2,
    FooterColumn3,
    FooterColumn4,
    CopyRight,
    AboutSec_1,
    MySkills,
    WhyChooseU,
)

def aboutus(request):
    navlogo = Navlogo.objects.all()
    navitem_1 = Navitem_1.objects.all()
    navitem_2 = Navitem_2.objects.all()
    navitem_3 = Navitem_3.objects.all()
    navitem_4 = Navitem_4.objects.all()
    navitem_5 = Navitem_5.objects.all()
    navitem_6 = Navitem_6.objects.all()
    navsubitem_1 = Navsubitem_1.objects.all()
    navsubitem_2 = Navsubitem_2.objects.all()
    navsubitem_3 = Navsubitem_3.objects.all()
    navsubitem_4 = Navsubitem_4.objects.all()
    navsubitem_5 = Navsubitem_5.objects.all()
    navsubitem_6 = Navsubitem_6.objects.all()
    homeBg = HomeBg.objects.all()
    leftMenu = LeftMenu.objects.all()
    latesttitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact = LeftContact.objects.all()
    clientlogo = ClientLogo.objects.all()
    whatwedo = WhatWedo.objects.all()
    servicetitleSub = Servicetitle.objects.all()
    seo = Services.objects.filter(category='seo')
    WebDesign = Services.objects.filter(category='WebDesign')
    SocialMediaMarketing = Services.objects.filter(category='SocialMediaMarketing')
    WebDevelopment = Services.objects.filter(category='WebDevelopment')
    EmailMarketing = Services.objects.filter(category='EmailMarketing')
    ADsManagement = Services.objects.filter(category='ADsManagement')
    creative = Creative.objects.all()
    contactus = ContactU.objects.all()
    gallery = Gallery.objects.all()
    galleryColumn1image = GalleryColumn1image.objects.all()
    galleryColumn2image = GalleryColumn2image.objects.all()
    galleryColumn3image = GalleryColumn3image.objects.all()
    galleryColumn4image = GalleryColumn4image.objects.all()
    footerColumn1 = FooterColumn1.objects.all()
    footerColumn2 = FooterColumn2.objects.all()
    footerColumn3 = FooterColumn3.objects.all()
    footerColumn4 = FooterColumn4.objects.all()
    copyRight = CopyRight.objects.all()
    aboutsec_1 = AboutSec_1.objects.all()
    myskills = MySkills.objects.all()
    whychooseme = WhyChooseU.objects.all()
    
    return render(request,'app/aboutus.html',
    {
        "navlogo"  :navlogo,
        "navitem_1" :navitem_1,
        "navitem_2" : navitem_2,
        "navitem_3" : navitem_3,
        "navitem_4" : navitem_4,
        "navitem_5" : navitem_5,
        "navitem_6" : navitem_6 ,
        "navsubitem_1" : navsubitem_1,
        "navsubitem_2" :  navsubitem_2,
        "navsubitem_3" :  navsubitem_3,
        "navsubitem_4" :  navsubitem_4,
        "navsubitem_5" :  navsubitem_5,
        "navsubitem_6" :  navsubitem_6,
        "leftMenu": leftMenu,
        "latesttitle": latesttitle,
        "lastestpicture":lastestpicture,
        "leftcontact": leftcontact,
        "footerColumn1" : footerColumn1,
        "footerColumn2" : footerColumn2,
        "footerColumn3" : footerColumn3,
        "footerColumn4" : footerColumn4,
        "copyRight" : copyRight,
        "aboutsec_1":aboutsec_1,
        "myskills":myskills,
        "whychooseme":whychooseme,
    })



def homePage(request):
    navlogo = Navlogo.objects.all()
    navitem_1 = Navitem_1.objects.all()
    navitem_2 = Navitem_2.objects.all()
    navitem_3 = Navitem_3.objects.all()
    navitem_4 = Navitem_4.objects.all()
    navitem_5 = Navitem_5.objects.all()
    navitem_6 = Navitem_6.objects.all()
    navsubitem_1 = Navsubitem_1.objects.all()
    navsubitem_2 = Navsubitem_2.objects.all()
    navsubitem_3 = Navsubitem_3.objects.all()
    navsubitem_4 = Navsubitem_4.objects.all()
    navsubitem_5 = Navsubitem_5.objects.all()
    navsubitem_6 = Navsubitem_6.objects.all()
    homeBg = HomeBg.objects.all()
    leftMenu = LeftMenu.objects.all()
    latesttitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact = LeftContact.objects.all()
    clientlogo = ClientLogo.objects.all()
    whatwedo = WhatWedo.objects.all()
    servicetitleSub = Servicetitle.objects.all()
    seo = Services.objects.filter(category='seo')
    WebDesign = Services.objects.filter(category='WebDesign')
    SocialMediaMarketing = Services.objects.filter(category='SocialMediaMarketing')
    WebDevelopment = Services.objects.filter(category='WebDevelopment')
    EmailMarketing = Services.objects.filter(category='EmailMarketing')
    ADsManagement = Services.objects.filter(category='ADsManagement')
    creative = Creative.objects.all()
    contactus = ContactU.objects.all()
    gallery = Gallery.objects.all()
    galleryColumn1image = GalleryColumn1image.objects.all()
    galleryColumn2image = GalleryColumn2image.objects.all()
    galleryColumn3image = GalleryColumn3image.objects.all()
    galleryColumn4image = GalleryColumn4image.objects.all()
    footerColumn1 = FooterColumn1.objects.all()
    footerColumn2 = FooterColumn2.objects.all()
    footerColumn3 = FooterColumn3.objects.all()
    footerColumn4 = FooterColumn4.objects.all()
    copyRight = CopyRight.objects.all()



    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactForm(yourName=yn,email=em,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            form = ContactUs()     
            return redirect ('/thankyou/')
    else:
        form = ContactUs()
    return render (request,'app/home.html',
    {
        "navlogo":navlogo,
        "navitem_1":navitem_1,
        "navitem_2" : navitem_2,
        "navitem_3" : navitem_3,
        "navitem_4" : navitem_4,
        "navitem_5" : navitem_5,
        "navitem_6" : navitem_6 ,
        "navsubitem_1" : navsubitem_1,
        "navsubitem_2" :  navsubitem_2,
        "navsubitem_3" :  navsubitem_3,
        "navsubitem_4" :  navsubitem_4,
        "navsubitem_5" :  navsubitem_5,
        "navsubitem_6" :  navsubitem_6,
        "homeBg": homeBg,
        "leftMenu":leftMenu,
        "latesttitle":latesttitle,
        "lastestpicture":lastestpicture,
        "leftcontact":leftcontact,
        "clientlogo" :clientlogo,
        "whatwedo":whatwedo,
        "servicetitleSub":servicetitleSub,
        "seo":seo,
        "WebDesign":WebDesign,
        "SocialMediaMarketing":SocialMediaMarketing,
        "WebDevelopment":WebDevelopment,
        "EmailMarketing":EmailMarketing,
        "ADsManagement":ADsManagement,
        "creative":creative,
        "contactus":contactus,
        "form":form,
        "gallery" : gallery,
        "galleryColumn1image" : galleryColumn1image,
        "galleryColumn2image" : galleryColumn2image,
        "galleryColumn3image" : galleryColumn3image,
        "galleryColumn4image" : galleryColumn4image,
        "footerColumn1" : footerColumn1,
        "footerColumn2" : footerColumn2,
        "footerColumn3" : footerColumn3,
        "footerColumn4" : footerColumn4,
        "copyRight" : copyRight,
        
        })


def thanks(request):
    navlogo = Navlogo.objects.all()
    navitem_1 = Navitem_1.objects.all()
    navitem_2 = Navitem_2.objects.all()
    navitem_3 = Navitem_3.objects.all()
    navitem_4 = Navitem_4.objects.all()
    navitem_5 = Navitem_5.objects.all()
    navitem_6 = Navitem_6.objects.all()
    navsubitem_1 = Navsubitem_1.objects.all()
    navsubitem_2 = Navsubitem_2.objects.all()
    navsubitem_3 = Navsubitem_3.objects.all()
    navsubitem_4 = Navsubitem_4.objects.all()
    navsubitem_5 = Navsubitem_5.objects.all()
    navsubitem_6 = Navsubitem_6.objects.all()
    leftMenu = LeftMenu.objects.all()
    latesttitle = Latesttitle.objects.all()
    lastestpicture = LastestPicture.objects.all()
    leftcontact = LeftContact.objects.all()
    footerColumn1 = FooterColumn1.objects.all()
    footerColumn2 = FooterColumn2.objects.all()
    footerColumn3 = FooterColumn3.objects.all()
    footerColumn4 = FooterColumn4.objects.all()
    copyRight = CopyRight.objects.all()
    return render (request,'app/thanks.html',
        {"navlogo":navlogo,
        "navitem_1":navitem_1,
        "navitem_2" : navitem_2,
        "navitem_3" : navitem_3,
        "navitem_4" : navitem_4,
        "navitem_5" : navitem_5,
        "navitem_6" : navitem_6 ,
        "navsubitem_1" : navsubitem_1,
        "navsubitem_2" :  navsubitem_2,
        "navsubitem_3" :  navsubitem_3,
        "navsubitem_4" :  navsubitem_4,
        "navsubitem_5" :  navsubitem_5,
        "navsubitem_6" :  navsubitem_6,
        "leftMenu": leftMenu,
        "latesttitle": latesttitle,
        "lastestpicture":lastestpicture,
        "leftcontact":    leftcontact,
        "footerColumn1" : footerColumn1,
        "footerColumn2" : footerColumn2,
        "footerColumn3" : footerColumn3,
        "footerColumn4" : footerColumn4,
        "copyRight" : copyRight,
        })



def contactus(request):
    if request.method == 'POST':
        form = ContactUs (request.POST)
        if form.is_valid():
            yn = form.cleaned_data['yourName']
            em = form.cleaned_data['email']
            pn = form.cleaned_data['Phonenumber']
            sb = form.cleaned_data['Subject']
            me = form.cleaned_data['Message']
            reg = ContactForm(yourName=yn,email=em,Phonenumber=pn,Subject=sb,Message=me)
            reg.save()
            messages.success(request,"Thanks For Contacting Us We will Response Shortly")
            form = ContactUs()
            return redirect ('/thanksyou/') 
    else:
        form = ContactUs()
    return render (request,'app/aboutus.html',{'form':form})



def navbar(request):
    return render (request,'app/navbar.html')