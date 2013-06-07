import subprocess
from os.path import join

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

from imagekit.models import ImageSpecField
from imagekit.models.fields import ProcessedImageField
from imagekit.processors import ResizeToFit, SmartResize

from zebra.models import StripeCustomer

import uuid

def get_unique_filename(filename):
    """
    Creates a unique filename.
    """
    ext = filename.split('.')[-1]
    return "%s.%s" % (uuid.uuid4(), ext)

def upload_to(instance, filename):
    """
    Upload path for profile photos.
    """
    return 'profiles/%d/%s' % (instance.id, get_unique_filename(filename))

# Attach a profile to the User model, and ensure that it's
# created whenever a new user is created.
class UserProfile(models.Model):
    # Required to associate with a unique user.
    user = models.OneToOneField(User)

    photo_count = models.PositiveIntegerField(default=0)

    CONTACT_TYPES = (
        ('N', 'None'),
        ('E', 'Embed'),
        ('M', 'Pop-up'),
    )
    contact_type = models.CharField(default='M', choices=CONTACT_TYPES, max_length=1)

    allow_about = models.BooleanField(default=True)

    enable_banner = models.BooleanField(default=True)

    full_width_navbar = models.BooleanField(default=False)

    show_get_started = models.BooleanField(default=True)

    page_width = models.PositiveIntegerField(default=930)

    title_size = models.PositiveIntegerField(default=30)

    thumbnail_dimension = models.PositiveIntegerField(default=225)

    font_size = models.FloatField(default=1.2)

    FONT_TYPES = (
        ('S', 'Sans Serif'),
        ('E', 'Serif'),
        ('M', 'Mono'),
    )
    font_type = models.CharField(default='S', choices=FONT_TYPES, max_length=1)

    ga_1 = models.PositiveIntegerField(null=True,
                                       blank=True)
    ga_2 = models.PositiveIntegerField(null=True,
                                       blank=True)
    
    copy_text = models.CharField(verbose_name='copyright text',
                                max_length=100,
                                blank=True)
    fullname = models.CharField(verbose_name='name',
                                max_length=30,
                                blank=True)
    location = models.CharField(verbose_name='location',
                                max_length=100,
                                blank=True)
    email = models.EmailField(verbose_name='contact email',
                              blank=True)
    about = models.TextField(verbose_name='about',
                             blank=True)
    phone = models.CharField(verbose_name='phone',
                             max_length=100, blank=True)

    background_color = models.CharField(max_length=6,
                                        default='F7F7F7')

    text_color = models.CharField(max_length=6,
                                  default='5E5E5E')

    text_color_hover = models.CharField(max_length=6,
                                        default='A1A1A1')

    website = models.URLField(max_length=500, blank=True)
    blog = models.URLField(max_length=500, blank=True)
    blog_name = models.CharField(max_length=15, blank=True)

    blogger = models.URLField(max_length=500, blank=True)
    deviantart = models.URLField(max_length=500, blank=True)
    digg = models.URLField(max_length=500, blank=True)
    facebook = models.URLField(max_length=500, blank=True)
    flickr = models.URLField(max_length=500, blank=True)
    google_plus = models.URLField(max_length=500, blank=True)
    linkedin = models.URLField(max_length=500, blank=True)
    myspace = models.URLField(max_length=500, blank=True)
    orkut = models.URLField(max_length=500, blank=True)
    pinterest = models.URLField(max_length=500, blank=True)
    tumblr = models.URLField(max_length=500, blank=True)
    twitter = models.URLField(max_length=500, blank=True)
    wordpress = models.URLField(max_length=500, blank=True)
    youtube = models.URLField(max_length=500, blank=True)

    picture = ProcessedImageField([ResizeToFit(width=200,
                                               height=250,
                                               upscale=False)],
                                  upload_to=upload_to,
                                  blank=True,
                                  null=True,
                                  verbose_name='Profile picture')

    banner = ProcessedImageField([ResizeToFit(width=500,
                                              height=80,
                                              upscale=False)],
                                 upload_to=upload_to,
                                 blank=True,
                                 null=True,
                                 verbose_name='Banner')

    favicon = ProcessedImageField([ResizeToFit(width=32,
                                               height=32,
                                               upscale=False)],
                                  upload_to=upload_to,
                                  blank=True,
                                  null=True,
                                  verbose_name='Favicon')

    edit_mode = models.BooleanField(default=True)

    # Slideshow-specific fields:

    enable_slideshow = models.BooleanField(default=False)

    slow_slideshow = models.BooleanField(default=True)

    skip_text = models.CharField(verbose_name='Skip text',
                                 max_length=300,
                                 blank=True)

    slideshow_image_1 = ProcessedImageField([ResizeToFit(width=settings.SLIDESHOW_IMAGE_WIDTH,
                                                         height=settings.SLIDESHOW_IMAGE_HEIGHT,
                                                         upscale=False)],
                                            upload_to=upload_to,
                                            null=True,
                                            blank=True)
    slideshow_thumbnail_1 = ImageSpecField([SmartResize(settings.SLIDESHOW_THUMBNAIL_WIDTH, settings.SLIDESHOW_THUMBNAIL_HEIGHT)],
                                           image_field='slideshow_image_1')

    slideshow_image_2 = ProcessedImageField([ResizeToFit(width=settings.SLIDESHOW_IMAGE_WIDTH,
                                                         height=settings.SLIDESHOW_IMAGE_HEIGHT,
                                                         upscale=False)],
                                            upload_to=upload_to,
                                            null=True,
                                            blank=True)
    slideshow_thumbnail_2 = ImageSpecField([SmartResize(settings.SLIDESHOW_THUMBNAIL_WIDTH, settings.SLIDESHOW_THUMBNAIL_HEIGHT)],
                                           image_field='slideshow_image_2')

    slideshow_image_3 = ProcessedImageField([ResizeToFit(width=settings.SLIDESHOW_IMAGE_WIDTH,
                                                         height=settings.SLIDESHOW_IMAGE_HEIGHT,
                                                         upscale=False)],
                                            upload_to=upload_to,
                                            null=True,
                                            blank=True)
    slideshow_thumbnail_3 = ImageSpecField([SmartResize(settings.SLIDESHOW_THUMBNAIL_WIDTH, settings.SLIDESHOW_THUMBNAIL_HEIGHT)],
                                           image_field='slideshow_image_3')
    
    def __unicode__(self):
        return u'Profile for %s' % self.user.username

    def save(self, *args, **kwargs):
        """
        Override save to delete the old picture if a new one is uploaded.
        """
        try:
            this = UserProfile.objects.get(pk=self.id)
            if this.picture and this.picture != self.picture:
                this.picture.delete(save=False)
        except: pass
        super(UserProfile, self).save(*args, **kwargs)

# Model associating domain names with users
class Domains(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30)
    domain = models.CharField(max_length=255)

# Create a Customer entry whenever a User is created.
class Customer(StripeCustomer):
    # Required to associate with a unique user.
    user = models.OneToOneField(User)
    ACCOUNT_LIMITS = (
        (settings.FREE_IMAGE_LIMIT, str(settings.FREE_IMAGE_LIMIT) + ' image uploads'),
        (settings.PREMIUM_IMAGE_LIMIT, str(settings.PREMIUM_IMAGE_LIMIT) + ' image uploads'),
        (settings.PROFESSIONAL_IMAGE_LIMIT, str(settings.PROFESSIONAL_IMAGE_LIMIT) + ' image uploads'),
    )
    account_limit = models.PositiveIntegerField(verbose_name='Account type',
                                                choices=ACCOUNT_LIMITS,
                                                default=settings.FREE_IMAGE_LIMIT)
    FILE_SIZE_LIMITS = (
        (settings.FREE_MAX_FILE_SIZE, str(settings.FREE_MAX_FILE_SIZE) + ' MB'),
        (settings.PREMIUM_MAX_FILE_SIZE, str(settings.PREMIUM_MAX_FILE_SIZE) + ' MB'),
        (settings.PROFESSIONAL_MAX_FILE_SIZE, str(settings.PROFESSIONAL_MAX_FILE_SIZE) + ' MB'),
    )
    max_file_size = models.PositiveIntegerField(verbose_name='Maximum upload size',
                                                choices=FILE_SIZE_LIMITS,
                                                default=settings.FREE_MAX_FILE_SIZE)

    def __unicode__(self):
        return u'Customer record for %s' % self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile to be associated with a User.
    """
    if created:
        UserProfile.objects.create(user=instance, fullname=instance.username)

def create_customer(sender, instance, created, **kwargs):
    """
    Create a Customer associated with a User.
    """
    if created:
        Customer.objects.create(user=instance)

def delete_banner_picture(sender, instance, *args, **kwargs):
    """
    Deletes the profile picture, banner, and favicon from the storage system upon
    UserProfile deletion.
    """
    if instance.picture:
        instance.picture.delete(save=False)
    if instance.banner:
        instance.banner.delete(save=False)
    if instance.favicon:
        instance.favicon.delete(save=False)

# On the User save signal, create a UserProfile and a Customer.
post_save.connect(create_user_profile, sender=User)
post_save.connect(create_customer, sender=User)

# When deleting a UserProfile, be sure to delete the profile picture.
post_delete.connect(delete_banner_picture, sender=UserProfile)
