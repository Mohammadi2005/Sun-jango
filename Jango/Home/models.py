from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name = "عنوان مقاله") # , null=True, blank=True
    text = models.TextField(help_text="Enter your article text.", verbose_name="متن")
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name ="تاریخ انتشار")
    updated_date = models.DateTimeField(auto_now=True ,verbose_name ="تاریخ بروز رسانی")
    is_show = models.BooleanField(default=True,verbose_name = "ایا مقاله نمایش داده شود")
    image = models.ImageField(upload_to="Home/image_article/",verbose_name ="تصویر")
    auther = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name ="نویسنده") # این باعث میشه که فقط فردی از بین کاربران ثبت نام شده در این سایت رو بشه به عنوان نویسنده انتخاب کرد
    categoreis = models.ManyToManyField(Category)
# "Person", on_delete=models.CASCADE یععنی برو به مدل person و اگر هم person حذف شد مقالاتش هم حذف بشه
    def __str__(self): # هر وقت کلاس فراخوانی بشه تایتلش برگردونده میشه که توی ادمین پنل این اتفاق میوفته و تایتل هر مقاله نمایش داده میشه
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

class Person(models.Model):
    first_name = models.CharField(max_length=200,verbose_name ="نام")
    last_name = models.CharField(max_length=200,verbose_name ="نام خانوادگی")
    email = models.EmailField(verbose_name ="ایمیل")
    age = models.IntegerField(default=0,verbose_name = "سن")
    website_url = models.URLField(max_length=200)
    score = models.FloatField()
    score_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
# max_digits=5 یعنی عدد حداکثر 5 رقم میتونه داشته باشه
# decimal_places=2 یعنی دو تا رقم اعشاری میتونه داشته باشه

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id} "

    class Meta:
        ordering = ['age']
        verbose_name = "شخص"
        verbose_name_plural = "اشخاص"