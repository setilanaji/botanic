from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings


class Plant(models.Model):
    name = models.CharField(_('Species Name'), max_length=100, blank=True, unique=True)
    family = models.CharField(_('Family Name'), max_length=60, blank=True, default='-')
    local = models.CharField(_('Local Name'), max_length=100, blank=True, default='-')
    synonym = models.CharField(_('Synonym Name'), max_length=200, blank=True, default='-')
    characteristic = models.TextField(_('Characteristic'), blank=True, default='-')
    image = models.ImageField(_('Picture'), upload_to='images/plants', blank=True)
    garden = models.ForeignKey( 'Garden', on_delete=models.CASCADE)
    date_added = models.DateTimeField(_('Date Added'), default=timezone.now)

    class Meta:
        db_table = 'plant'
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'


class Garden(models.Model):
    name = models.CharField(_('Collection Name'), max_length=100, blank=True, unique=True)
    desc = models.TextField(_('Description'), blank=True, default='-')
    date_added = models.DateTimeField(_('Date Build'), default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'garden'
        verbose_name = 'Garden'
        verbose_name_plural = 'Gardens'


class Facility(models.Model):
    TYPE_CHOICE = (
        ('GN', 'General'),
        ('OF', 'Office'),
        ('SH', 'Shop'),
        ('RS', 'Restaurant'),
        ('PR', 'Pray'),
        ('AT', 'Attraction')
    )
    name = models.CharField(_('Facility Name'), max_length=50, blank=True)
    desc = models.TextField(_('Description'), blank=True, default='-')
    date_added = models.DateTimeField(_('Date Build'), default=timezone.now)
    type = models.CharField(_('Type'), max_length=3, choices=TYPE_CHOICE)

    class Meta:
        db_table = 'facility'
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'


class News(models.Model):
    title = models.CharField(_('Title'), max_length=100, blank=True)
    content = models.TextField(_('Content'), blank=True, default='-')
    date_added = models.DateTimeField(_('Date Added'), default=timezone.now)

    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'


# class Account(models.Model):
#     name = models.CharField(_('Name'), max_length=200)
#     username = models.CharField(_('Username'), max_length=200, unique=True)
#     email = models.EmailField(_('Email'), max_length=200)
#     password = models.CharField(_('Password'), max_length=200)
#     profile = models.ImageField(_('Profile Image'), upload_to='images/users/profile', blank=True)
#     date_join = models.DateTimeField(_('Date Joined'), default=timezone.now)
#
#     class Meta:
#         db_table = 'user'
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
