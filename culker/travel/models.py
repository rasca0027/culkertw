# -*- coding: utf-8 -*-
from django.db import models

class Seed(models.Model):
    LOC_CHOICE = (
        ('N', 'north'),
        ('M', 'middle'),
        ('S', 'south'),
        ('E', 'east'),
        ('O', 'other'),
    )

    name = models.CharField(max_length=30)
    quote = models.CharField(max_length=60)
    location = models.CharField(choices=LOC_CHOICE, max_length=20)
    intro = models.TextField()
    avatar = models.CharField(max_length=1000)
    banner1 = models.CharField(max_length=1000)
    banner2 = models.CharField(max_length=1000)
    banner3 = models.CharField(max_length=1000)
    feature = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Trip(models.Model):
    CANCEL_CH = (('flexible', '靈活'), ('strict', '嚴格'))
    
    name = models.CharField(max_length=30)
    seed = models.ForeignKey(Seed)
    time = models.CharField(max_length=50)
    language = models.CharField(max_length=25)
    duration = models.CharField(max_length=20)
    people = models.IntegerField(default=1)
    fee = models.IntegerField()
    cancel = models.CharField(choices=CANCEL_CH, max_length=20)
    short_descp = models.TextField()
    cover_photo = models.CharField(max_length=1000)
    header1 = models.CharField(max_length=30, blank=True)
    paragraph1 = models.TextField()
    header2 = models.CharField(max_length=30, blank=True)
    paragraph2 = models.TextField()
    header3 = models.CharField(max_length=30, blank=True)
    paragraph3 = models.TextField()
    timetable = models.TextField()
    note = models.TextField()
    pic1 = models.CharField(max_length=1000)
    pic2 = models.CharField(max_length=1000)
    pic3 = models.CharField(max_length=1000)
    enroll_form = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name
