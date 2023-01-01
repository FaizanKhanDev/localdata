from django.contrib import admin
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
    WhyChooseU

)


@admin.register(Navlogo)
class NavlogoAdmin(admin.ModelAdmin):
    list_display = ['id','navlogo']



@admin.register(Navitem_1)
class Navitem_1Admin(admin.ModelAdmin):
    list_display = ['id','navitem_1']




@admin.register(Navitem_2)
class Navitem_2Admin(admin.ModelAdmin):
    list_display = ['id','navitem_2']




@admin.register(Navitem_3)
class Navitem_3Admin(admin.ModelAdmin):
    list_display = ['id','navitem_3']




@admin.register(Navitem_4)
class Navitem_4Admin(admin.ModelAdmin):
    list_display = ['id','navitem_4']




@admin.register(Navitem_5)
class Navitem_5Admin(admin.ModelAdmin):
    list_display = ['id','navitem_5']



    
@admin.register(Navitem_6)
class Navitem_6Admin(admin.ModelAdmin):
    list_display = ['id','navitem_6']




@admin.register(Navsubitem_1)
class Navsubitem_1Admin(admin.ModelAdmin):
    list_display = ['id','navsubitem_1']




@admin.register(Navsubitem_2)
class Navitem_2Admin(admin.ModelAdmin):
    list_display = ['id','navsubitem_2']




@admin.register(Navsubitem_3)
class Navsubitem_3Admin(admin.ModelAdmin):
    list_display = ['id','navsubitem_3']




@admin.register(Navsubitem_4)
class Navsubitem_4Admin(admin.ModelAdmin):
    list_display = ['id','navsubitem_4']




@admin.register(Navsubitem_5)
class Navsubitem_5Admin(admin.ModelAdmin):
    list_display = ['id','navsubitem_5']



@admin.register(Navsubitem_6)
class Navsubitem_6Admin(admin.ModelAdmin):
    list_display = ['id','navsubitem_6']


@admin.register(HomeBg)
class HomeBgAdmin(admin.ModelAdmin):
    list_display = ['id','homebg','bgtitle','homebtn']


@admin.register(LeftMenu)
class LeftMenuAdmin(admin.ModelAdmin):
    list_display = ['id','title','descriptions']


@admin.register(Latesttitle)
class LatesttitleAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(LastestPicture)
class LastestPictureAdmin(admin.ModelAdmin):
    list_display = ['id','latestImg']

@admin.register(LeftContact)
class LeftContactAdmin(admin.ModelAdmin):
    list_display = ['id','title','phone','email','copyRight']


@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ['id','img']



@admin.register(WhatWedo)
class WhatWedoAdmin(admin.ModelAdmin):
    list_display = ['id','title']


@admin.register(Servicetitle)
class ServicetitleAdmin (admin.ModelAdmin):
    list_display = ['id','title','subtitle','subtitle1']

@admin.register(Services)
class ServicesAdmin (admin.ModelAdmin):
    list_display = ['id','title','description','category']

@admin.register(ServicesBtn)
class ServicesBtnAdmin(admin.ModelAdmin):
    list_display = ['id','btn']


@admin.register(Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = ['id','title1','title2','description1','description2','img','btn']


@admin.register(ContactU)
class ContactUAdmin(admin.ModelAdmin):
    list_display = ['id','maintitle','title1','title2','phoneNumber','Email']

@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
    list_display = ['id','yourName','email','Phonenumber','Subject','Message',]



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(GalleryColumn1image)
class GalleryColumn1imageAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(GalleryColumn2image)
class GalleryColumn2imageAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(GalleryColumn3image)
class GalleryColumn3imageAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(GalleryColumn4image)
class GalleryColumn4imageAdmin(admin.ModelAdmin):
    list_display = ['id','img']

@admin.register(FooterColumn1)
class FooterColumn1Admin(admin.ModelAdmin):
    list_display = ['id','title','item1','item2','item3','item4','item5']



@admin.register(FooterColumn2)
class FooterColumn2Admin(admin.ModelAdmin):
    list_display = ['id','title','item1','item2','item3','item4','item5']

@admin.register(FooterColumn3)
class FooterColumn3Admin(admin.ModelAdmin):
    list_display = ['id','title','item1','item2','item3','item4','item5']


@admin.register(FooterColumn4)
class FooterColumn4Admin(admin.ModelAdmin):
    list_display = ['id','title','item1','item2','item3']




@admin.register(CopyRight)
class CopyRightAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(AboutSec_1)
class AboutSec_1Admin(admin.ModelAdmin):
    list_display = ['id','title','subtitle','description','subdescription','btn','img']

@admin.register(MySkills)
class MySkillsAdmin(admin.ModelAdmin):
    list_display = ['id',
    'img','title','skillsName1','progress','skillsName2',
    'progress2','skillsName3','progress3',
    'skillsName4','progress4','skillsName5',
    'progress5','skillsName6','progress6',
    'skillsName7','progress7','skillsName8',
    'progress8','skillsName9','progress8']

@admin.register(WhyChooseU)
class WhyChooseUAdmin(admin.ModelAdmin):
    list_display = ['id','maintitle','subtitle1','description',
    'subtitle2','description2','subtitle3','description3','subtitle4','description4',
    'subtitle5','description5','subtitle6','description6']