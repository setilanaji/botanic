from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from plant.utils import random_string_generator
from django.db.models.signals import pre_save


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Plant(models.Model):
    name = models.CharField(_('Species Name'), max_length=100, blank=True, unique=True)
    # family = models.CharField(_('Family Name'), max_length=60, blank=True)
    slug = models.SlugField(_('slug'), null=True, blank=True)
    local = models.CharField(_('Local Name'), max_length=100, blank=True)
    synonym = models.CharField(_('Synonym Name'), max_length=200, blank=True)
    # origin = models.CharField(_('Origin'), max_length=100, blank=True)
    characteristic = models.TextField(_('Characteristic'), blank=True)
    gardens = models.ManyToManyField('Garden', related_name='plants', blank=True)
    image = models.ImageField(_('Main Picture'), upload_to='images/plants', blank=True)
    date_added = models.DateTimeField(_('Date Added'), default=timezone.now)

    @property
    def a_property_method(self):
        return "I am a Property Method"

    def an_instance_method(self):
        return "I am a Instance Method"

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'plant'
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'


class Photo(models.Model):
    plant = models.ForeignKey('Plant', related_name='more_photos', on_delete=models.CASCADE, null=True)
    imagefile = models.ImageField(_('More Picture'), upload_to="images/plants/more")

    def natural_key(self):
        return self.imagefile

    def __str__(self):
        return "%s - %s " % (self.plant.name, self.imagefile)


class Garden(models.Model):
    name = models.CharField(_('Garden Name'), max_length=100, blank=True)
    slug = models.SlugField(_('slug'), null=True, blank=True)
    desc = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Picture'), upload_to='images/gardens', blank=True)
    location_long = models.FloatField(_('Longitude Location'), blank=True, default=0)
    location_lat = models.FloatField(_('Latitude Location'), blank=True, default=0)
    date_added = models.DateTimeField(_('Date Added'), default=timezone.now)
    # botanic = models.ForeignKey('Botanic', related_name='gardens', on_delete=models.CASCADE, null=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'garden'
        verbose_name = 'Garden'
        verbose_name_plural = 'Gardens'

#
# class Botanic(models.Model):
#     name = models.CharField(_('Name'), max_length=100, blank=True)
#     description = models.TextField(_('Description'), blank=True)
#     date_added = models.DateTimeField(_('Date Build'), default=timezone.now)
#     address = models.CharField(_('Address'), max_length=200, blank=True)
#     website = models.CharField(_('Website'), max_length=100, blank=True)
#     image = models.ImageField(_('Picture'), upload_to='images/botanics', blank=True)
#
#     def natural_key(self):
#         return self.name
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'botanic'
#         verbose_name = 'Botanic'
#         verbose_name_plural = 'Botanics'


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100, blank=True)
    slug = models.SlugField(_('slug'), null=True, blank=True)
    description = models.TextField(_('Description'), blank=True)
    plants = models.ManyToManyField('Plant', related_name='categories', blank=True)
    image = models.ImageField(_('Picture'), upload_to='images/categories', blank=True)
    date_added = models.DateTimeField(_('Date Added'), default=timezone.now)

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


pre_save.connect(slug_generator, sender=Plant)
pre_save.connect(slug_generator, sender=Garden)
pre_save.connect(slug_generator, sender=Category)

