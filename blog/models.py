from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django_jalali.db import models as jmodels


#my manager

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='P')
# Create your models here.

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self',default=None, blank=True, null=True, related_name='children', on_delete=models.SET_NULL, verbose_name="دسته بندی والد")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ دسته بندی")
    status = models.BooleanField(default=True, verbose_name="فعال")
    position = models.IntegerField(verbose_name="پوزیشن")


    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','-position']

    def __str__(self):
        return self.title

    objects = CategoryManager()

class Article(models.Model):
    """
    Model representing an article
    """
    STATUS_CHOICES = (
        ('D', 'پیش نویس'),
        ('P', 'منتشر شده'),
    )

    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100,unique=True, verbose_name = "اسلاگ ")
    category = models.ManyToManyField(Category,verbose_name="دسته بندی",related_name="articles")
    description = models.TextField( verbose_name = "توضیحات ")
    thumbnail = models.ImageField(upload_to = "images", verbose_name = "تصویر ")
    published = jmodels.jDateTimeField(default=timezone.localtime, verbose_name = "زمان انتشار ")
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name = "زمان ساخت ")
    updated = jmodels.jDateTimeField(auto_now=True, verbose_name = "زمان اپدیت ")
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, verbose_name = "وضعیت انتشار ")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        ordering = ['published']
    def __str__(self):
        return self.title

    def category_publish(self):
        return self.category.filter(status=True)

    def article_publish(self):
        return self.objects.filter(status='p')

    def thumpnail_tag(self):
        if self.thumbnail != None:
            return format_html('<img src="{0}" width="100" height="70" />'.format(self.thumbnail.url))
        else:
            return "No Image"


    objects = ArticleManager()