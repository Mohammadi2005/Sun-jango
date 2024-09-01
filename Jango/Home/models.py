from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(help_text="Enter your article text.")
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_show = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    auther = models.ForeignKey("Person", on_delete=models.CASCADE)
# "Person", on_delete=models.CASCADE یععنی برو به مدل person و اگر هم person حذف شد مقالاتش هم حذف بشه
    def __str__(self): # هر وقت کلاس فراخوانی بشه تایتلش برگردونده میشه که توی ادمین پنل این اتفاق میوفته و تایتل هر مقاله نمایش داده میشه
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    website_url = models.URLField(max_length=200)
    score = models.FloatField()
    score_2 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
# max_digits=5 یعنی عدد حداکثر 5 رقم میتونه داشته باشه
# decimal_places=2 یعنی دو تا رقم اعشاری میتونه داشته باشه

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
