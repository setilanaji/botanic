from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Plant(models.Model):
    name = models.CharField(_('Species Name'), max_length=100, blank=True, unique=True)
    family = models.CharField(_('Family Name'), max_length=60, blank=True)
    local = models.CharField(_('Local Name'), max_length=100, blank=True)
    synonym = models.CharField(_('Synonym Name'), max_length=200, blank=True)
    characteristic = models.TextField(_('Characteristic'), blank=True)
    image = models.ImageField(_('Picture'), upload_to='images/plants', blank=True)
    garden = models.ForeignKey('Garden', on_delete=models.CASCADE)
    date_added = models.DateTimeField(_('Date Added'), default=timezone.now)

    class Meta:
        db_table = 'plant'
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'


class Garden(models.Model):
    name = models.CharField(_('Collection Name'), max_length=100, blank=True, unique=True)
    desc = models.TextField(_('Description'), blank=True)
    date_added = models.DateTimeField(_('Date Build'), default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'garden'
        verbose_name = 'Garden'
        verbose_name_plural = 'Gardens'