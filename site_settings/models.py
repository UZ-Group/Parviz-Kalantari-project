from django.db import models
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class SiteSetting(models.Model):
    bio = RichTextUploadingField(verbose_name='بیوگرافی هنرمند')
    image = models.ImageField(upload_to='images/site', verbose_name='عکس هنرمند(بیو)')
    contact_us =  RichTextUploadingField(verbose_name='ارتباط با ما')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'بیوگرافی و ارتباط با ما'
    
    def image_tag(self):
        return format_html("<img width=100 height=75 style='border-radius: 10px;' src='{}'>".format(self.image.url))
    image_tag.short_description = "عکس"