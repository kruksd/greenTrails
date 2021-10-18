from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class CampModel(models.Model):
    title = models.CharField(blank=False, max_length=100, unique=True)
    description = models.CharField(blank=False, max_length=2000)
    image = models.ImageField(blank=False,default="user-default.png")
    camp_season=models.CharField(max_length=200,blank=False,null=False)
    camp_latest = models.BooleanField(blank=False, default=True)
    camp_days = models.SmallIntegerField(blank=False)
    camp_nights = models.SmallIntegerField(blank=False)
    camp_altitude = models.IntegerField(blank=False)
    camp_choices = (('easy', 'EASY'), ('medium', 'MEDIUM'), ('hard', 'HARD'))
    camp_difficulty = models.CharField(blank=False, max_length=20, choices=camp_choices, default=camp_choices[0])
    camp_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    camp_note = models.CharField(blank=False, max_length=250)
    camp_brochure = models.FileField(blank=False)
    camp_packages = models.TextField(blank=False,
                                help_text='Enter colon(;) seperated packages, E.g Kedarnath To Kedarnath, 15000;'
                                          'Jammu to Jammu, 15000')
    camp_dates = models.TextField(blank=False, help_text='Enter colon(;) seperated dates, E.g MAR 6 2021; MAY 22 2021')
    camp_about = models.TextField(blank=False)
    camp_schedules = models.TextField(blank=False,
                                 help_text='Enter colon(;) seperated schedules for each day, E.g Departure form '
                                           'Vadodara 1:00 am; Arrival at Vadodara')
    camp_places_to_visit = models.TextField(blank=False, help_text='Enter colon(;) seperated places')
    camp_activities = models.TextField(blank=False, help_text='Enter colon(;) seperated activities')
    camp_inclusions = models.TextField(blank=False, help_text='Enter colon(;) seperated inclusions')
    camp_exclusions = models.TextField(blank=False, help_text='Enter colon(;) seperated exclusions')
    camp_carried_things = models.TextField(blank=False, help_text='Enter colon(;) seperated things')
    camp_guidelines = models.TextField(blank=False, help_text='Enter colon(;) seperated guidelines')
    camp_instructions = models.TextField(blank=False, help_text='Enter colon(;) seperated instructions')
    camp_suggestions = models.TextField(blank=True, help_text='Enter colon(;) seperated suggestions')
    camp_photos=models.TextField(blank=False,null=False,max_length=2000)
    camp_objects = models.manager

    def __str__(self):
        return self.title

class aboutModel(models.Model):
    about_latest = models.BooleanField(blank=False, default=True)
    about_para = models.CharField(max_length=5000,null=False,blank=False)
    about_image = models.ImageField(blank=False,null=False,default="20210706_170841-01.jpeg")
    mission_para = models.CharField(max_length=5000,null=False,blank=False)
    vision_para = models.CharField(max_length=5000,null=False,blank=False)
    objective_para = models.CharField(max_length=5000,null=False,blank=False)
    def __str__(self):
        return 'About Us'
class youTubeModel(models.Model):
    video_link = models.CharField(max_length=5000,null=False,blank=False)

class instaLinkModel(models.Model):
    insta_link1 = models.CharField(blank=False,null=False,max_length=2000)
    insta_link2 = models.CharField(blank=False,null=False,max_length=2000)
    insta_link3 = models.CharField(blank=False,null=False,max_length=2000)
    def __str__(self):
        return 'Instagram'

class Conformation(models.Model):
    title = models.CharField(max_length=200, default="")
    package = models.CharField(max_length=200, default="")
    date = models.CharField(max_length=100, default="")
    rate = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=300, default="")
    id_proof = models.ImageField(blank=False, upload_to='images/formdata')
    photo = models.ImageField(blank=False, upload_to='images/formdata')
    bdate = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=10, default="")
    blood_group = models.CharField(max_length=5, default="")
    weight = models.IntegerField(default="")
    occupation = models.CharField(max_length=100, default="")
    organization = models.CharField(max_length=300, default="")
    guardian_name = models.CharField(max_length=200, default="")
    guardian_email = models.CharField(max_length=200, default="")
    guardian_mobile = models.CharField(max_length=20, default="")
    participated_where = models.CharField(max_length=300, default="")
    disease_phobia = models.CharField(max_length=300, default="")
    reference = models.CharField(max_length=50, default="")
    online_name = models.CharField(max_length=300, default="", blank=True)
    online_email = models.CharField(max_length=200, default="", blank=True)
    online_mobile = models.CharField(max_length=20, default="", blank=True)
    objects = models.manager

    def __str__(self):
        return self.name + " -  " + self.title