from django.db import models

# Create your models here.


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, phone, username, password, role):
        if not phone:
            raise ValueError('please enter an phone')

        if not username:
            raise ValueError('please enter an username')

        user = self.model(phone=phone, username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password,  role='ADMIN'):
       user = self.create_user(phone, username, password, role)
       user.is_admin = True
       user.save(using=self._db)
       return user


class User(AbstractBaseUser):
    ROLE_CHOICES =(
        ('SELLER', 'Seller'),
        ('COSTUMER', 'costumer'),
        ('ADMIN', 'admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    username = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    user_id = models.AutoField(primary_key=True, auto_created=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




class CostumerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=200)
    address = models.TextField()
    verify_phone = models.BooleanField(default=False)


def save_profile_user(sender, instance, **kwargs):
    if kwargs['created'] and instance.role == "COSTUMER":
        profile_user = CostumerProfile(user=instance)
        profile_user.save()


post_save.connect(save_profile_user, sender=User)




class BakeryType(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type


class SellerProfile(models.Model):
    STATUS_CHOICES =(
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    )
    type = models.ManyToManyField(BakeryType, blank=True, related_name="typeof")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    first_name = models.CharField(max_length=50)
    Holiday = models.CharField(max_length=3, choices=STATUS_CHOICES)
    last_name = models.CharField(max_length=50)
    bakeryPhone = models.IntegerField(null=True)
    city = models.CharField(max_length=200)
    address = models.TextField()
    verify_phone = models.BooleanField(default=False)
    def __str__(self):
        return self.user.phone


def save_seller_profile(sender, instance, **kwargs):
    if kwargs['created'] and instance.role == "SELLER":
        seller_profile = SellerProfile(user=instance)
        seller_profile.save()


post_save.connect(save_seller_profile, sender=User)






