from django.db import models
from accounts.models import User
from administrator.models import post
from django.forms import ModelForm

# Create your models here.


class Cart(models.Model):
    product = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="تعداد")
    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد خرید"


class cartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']