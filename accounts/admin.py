from django.contrib import admin
from .models import BakeryType, SellerProfile,CostumerProfile
# Register your models here.
admin.site.register(BakeryType)
admin.site.register(SellerProfile)
admin.site.register(CostumerProfile)
