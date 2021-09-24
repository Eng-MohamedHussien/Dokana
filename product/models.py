from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import RegexValidator


from PIL import Image
from io import BytesIO
import sys


def generate_client_business_logo_path(instance, filename):
        return f'clients/{instance.brand_name}/{filename}'

class Client(models.Model):
    name = models.CharField(max_length=256, verbose_name='اسم التاجر')
    brand_name = models.CharField(max_length=256, verbose_name='اسم الصفحة او المحل')
    terms_conditions = models.TextField(verbose_name='شروط واحكام استرجاع المنتج')
    has_delivery = models.BooleanField(verbose_name='خدمة توصيل', default=True)
    address = models.CharField(max_length=256, verbose_name='عنوانه او عنوان محله')
    facebook_link = models.URLField(verbose_name='لينك لصفحة الفيسبوك (اختيارى)', blank=True, null=True)
    email = models.EmailField(verbose_name='البريد الالكترونى (اختيارى)', blank=True, null=True)
    mobile_number_regex = RegexValidator(regex=r"([0]{1}[1]{1}[0-9]{9})")
    mobile_number = models.CharField(max_length=11, blank=True, null=True, verbose_name= 'رقم المحمول (اختيارى)', validators=[mobile_number_regex]) 
    logo = models.ImageField(upload_to = generate_client_business_logo_path, verbose_name='لوجو صفحة الفيسبوك او الموقع او المحل (اختيارى)', blank=True, null=True)
    commission = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='عمولة دكانه', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="توقيت الاضافة")
    updated = models.DateTimeField(auto_now=True, verbose_name="توقيت اخر تعديل")

    class Meta:
        verbose_name = 'تاجر'
        verbose_name_plural = 'تجار'
    
    def __str__(self):
        return self.brand_name


def generate_category_image_path(instance, filename):
        return f'categories/{instance.name}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True, verbose_name="اسم الصنف")
    slug = models.SlugField(max_length=128, unique=True, db_index=True, allow_unicode=True, verbose_name="عنوان الصنف")
    image = models.ImageField(upload_to=generate_category_image_path, verbose_name='صورة للصنف', null=True, blank=True)
    design = models.ImageField(upload_to=generate_category_image_path, verbose_name='صورة تسويقية للصنف', null=True, blank=True)
    discount_design = models.ImageField(upload_to=generate_category_image_path, verbose_name='صورة خصومات للصنف', null=True, blank=True)

    class Meta:
        verbose_name = "صنف"
        verbose_name_plural = "الاصناف"


    def get_absolute_url(self):
        return reverse('product:show_category_items', kwargs={'category_slug': self.slug})
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='اختر الصنف')
    name = models.CharField(max_length=256, unique=True, db_index=True, verbose_name='اسم المنتج')
    slug = models.SlugField(max_length=256, unique=True, db_index=True, allow_unicode=True, verbose_name='عنوان المنتج')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='السعر / السعر بعد الخصم')
    discount = models.BooleanField(default=False, verbose_name='عليه تخفيض')
    price_before_discount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='السعر قبل الخصم', blank=True, null=True)
    available = models.BooleanField(default=True, verbose_name="متاح")
    overview = models.TextField(verbose_name='شرح المنتج', blank=True, null=True)
    details = models.TextField(verbose_name="وصف المنتج", blank=True, null=True) 
    how_to_use = models.TextField(verbose_name="كيفية الاستخدام", blank=True, null=True)
    video = models.URLField(blank=True, null=True, verbose_name='فيديو للمنتج')
    created = models.DateTimeField(auto_now_add=True, verbose_name="توقيت الاضافة")
    updated = models.DateTimeField(auto_now=True, verbose_name="توقيت اخر تعديل")
    merchant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='products', verbose_name='المورد', blank=True, null=True)


    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ('-created',)


    def get_absolute_url(self):
        return reverse('product:product_details', kwargs={'product_slug': self.slug})
    

    def get_album_master_scene_image(self):
        return ProductImage.objects.get(product__id=self.id, is_master_scene=True).image.url


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
 

def generate_album_path(instance, filename):
        return f'albums/{instance.product.name}/gallery/{filename}'


@receiver(pre_save, sender=Product)
def update_youtube_link(sender, instance, **kwargs):
    if instance.video != None:
        video_id = instance.video[instance.video.index("?v=") + 3 : ]
        new_youtube_video = "https://www.youtube.com/embed/" + video_id
        instance.video = new_youtube_video


class ProductImage(models.Model):
    image = models.ImageField(upload_to=generate_album_path, verbose_name='صور للمنتج')
    is_master_scene = models.BooleanField(default=False, verbose_name='واجهة عرض')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='album')
    
    def save(self, *args, **kwargs):
        imageTemproary = Image.open(self.image)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (300,300) ) 
        imageTemproaryResized.save(outputIoStream , format='JPEG', quality=80)
        outputIoStream.seek(0)
        self.image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        super(ProductImage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'صورة للالبوم'
        verbose_name_plural = 'صور الالبوم'