from django.db import models
from django.contrib.auth.models import User

class Navlogo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    navlogo = models.TextField(max_length=100)
    def __str__(self):
        return str(self.id) 

# === nav main Items === #
class Navitem_1(models.Model):
    navitem_1 = models.TextField(max_length=100)
    def __str__(self):
        return str(self.id)

class Navitem_2(models.Model):
    navitem_2 = models.TextField(max_length=100)
    def __str__(self):
        return str(self.id)

class Navitem_3(models.Model):
    navitem_3 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navitem_4(models.Model):
    navitem_4 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)
        
class Navitem_5(models.Model):
    navitem_5 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navitem_6 (models.Model):
    navitem_6 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

# === nav main Items End === #

# === nav Subitems Items  === #

class Navsubitem_1(models.Model):
    navsubitem_1 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navsubitem_2(models.Model):
    navsubitem_2 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navsubitem_3(models.Model):
    navsubitem_3 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navsubitem_4(models.Model):
    navsubitem_4 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navsubitem_5(models.Model):
    navsubitem_5 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)

class Navsubitem_6 (models.Model):
    navsubitem_6 = models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)
# === nav Subitems Items End === #

# === home BackGround === #
class HomeBg(models.Model):
    homebg = models.ImageField(upload_to='allimages')
    bgtitle = models.TextField(max_length=1000)
    homebtn =  models.TextField(max_length=100)
    def __str__(self):
        return str (self.id)
# === home BackGround === #

# === Nav Left Slide Menu === #

class LeftMenu(models.Model):
    title = models.TextField(max_length=100)
    descriptions = models.TextField(max_length=100)
    def _str__(self):
        return self(self.id)


class Latesttitle(models.Model):
    title = models.TextField(max_length=100)
    def _str__(self):
        return self(self.id)


class LastestPicture(models.Model):
    latestImg =  models.ImageField(upload_to='allimages')
    def _str__(self):
        return self(self.id)


class LeftContact(models.Model):
    title = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    copyRight = models.TextField(max_length=100)
    def _str__(self):
        return self(self.id)
# === Nav Left Slide Menu End === #

# === Client Logo Slide Menu  === #
class ClientLogo(models.Model):
    img =  models.ImageField(upload_to='allimages')


# === Client Logo  Slide  End === #



# === What's Can Do === #

class WhatWedo(models.Model):
    title = models.TextField(max_length=50)
# === What's Can Do === #
class Servicetitle(models.Model):
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=100)
    subtitle1 = models.TextField(max_length=100)
# == services CATEGORY === #


SERVICES_CATEGORY_CHOICES = (
    ('seo','SEO'),
    ('WebDesign','WEBDESIGN'),
    ('SocialMediaMarketing','SOCIALMEDIAMARKETING'),
    ('WebDevelopment','WEBDEVELOPMENT'),
    ('EmailMarketing','EMAILMARKETING'),
    ('ADsManagement','ADMANAGEMENT'),
)

class Services(models.Model):
    title = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    category = models.CharField(choices=SERVICES_CATEGORY_CHOICES,max_length=100)

class ServicesBtn(models.Model):
    btn = models.TextField(max_length=10)


# == services CATEGORY === #

# ==== Creative Section === # 

class Creative (ServicesBtn):
    title1 = models.TextField(max_length=100)
    title2 = models.TextField(max_length=100)
    description1 = models.TextField(max_length=250)
    description2 = models.TextField(max_length=250)
    img = models.ImageField(upload_to='allimages')




# ==== Creative Section === # 

# ==== Contact Section === # 

class ContactU(models.Model):
    maintitle = models.CharField(max_length=30)
    title1 = models.CharField(max_length=50) 
    title2 = models.CharField(max_length=50) 
    phoneNumber = models.CharField(max_length=20)
    Email = models.EmailField()

class ContactForm(models.Model):
    yourName = models.TextField(max_length=50)
    email = models.EmailField()
    Phonenumber = models.CharField(max_length=20)
    Subject = models.CharField(choices=SERVICES_CATEGORY_CHOICES,max_length=100)
    Message = models.CharField(max_length=400)
    btn = models.CharField(max_length=10)


# ==== Contact Section === # 
# ==== Gallery Section === # 


class Gallery(models.Model):
    title = models.TextField(max_length=100)


class GalleryColumn1image(models.Model):
    img = models.ImageField(upload_to='allimages')

class GalleryColumn2image(models.Model):
    img = models.ImageField(upload_to='allimages')

class GalleryColumn3image(models.Model):
    img = models.ImageField(upload_to='allimages')

class GalleryColumn4image(models.Model):
    img = models.ImageField(upload_to='allimages')


# ==== Gallery Section === # 

# ==== footer Section === # 

class FooterColumn1(models.Model):
    title = models.CharField(max_length=100)
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)
    item5 = models.CharField(max_length=100)
  

class FooterColumn2(models.Model):
    title = models.CharField(max_length=100)
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)
    item5 = models.CharField(max_length=100)



class FooterColumn3(models.Model):
    title = models.CharField(max_length=100)
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)
    item5 = models.CharField(max_length=100)


class FooterColumn4(models.Model):
    title = models.CharField(max_length=100)
    item1 = models.CharField(max_length=100)
    item2 = models.CharField(max_length=100)
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)


class CopyRight(models.Model):
    title = models.CharField(max_length=100)

# ==== footer Section === # 



# ==== About Section === # 

class AboutSec_1(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    subdescription = models.CharField(max_length=400)
    btn = models.CharField(max_length=10)
    img = models.ImageField(upload_to='allimages')



class MySkills(models.Model):
    img = models.ImageField(upload_to='allimages')
    title = models.CharField(max_length=100)
    skillsName1 = models.CharField(max_length=100)
    progress = models.CharField(max_length=10)
    skillsName2 = models.CharField(max_length=100)
    progress2 = models.CharField(max_length=10)
    skillsName3 = models.CharField(max_length=100)
    progress3 = models.CharField(max_length=10)
    skillsName4 = models.CharField(max_length=100)
    progress4 = models.CharField(max_length=10)
    skillsName5 = models.CharField(max_length=100)
    progress5 = models.CharField(max_length=10)
    skillsName6 = models.CharField(max_length=100)
    progress6 = models.CharField(max_length=10)
    skillsName7 = models.CharField(max_length=100)
    progress7 = models.CharField(max_length=10)
    skillsName8 = models.CharField(max_length=100)
    progress8 = models.CharField(max_length=10)
    skillsName9 = models.CharField(max_length=100)
    progress9 = models.CharField(max_length=10)



class WhyChooseU(models.Model):
    maintitle = models.CharField(max_length=100)
    subtitle1 = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    subtitle2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    subtitle3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    subtitle4 = models.CharField(max_length=100)
    description4 = models.CharField(max_length=100)
    subtitle5 = models.CharField(max_length=100)
    description5 = models.CharField(max_length=100)
    subtitle6 = models.CharField(max_length=100)
    description6 = models.CharField(max_length=100)

# ==== About Section === # 








