from django.db import models

# Create your models here.


class post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=100)
    description = models.TextField()
    count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
