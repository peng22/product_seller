from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=35)
    price=models.FloatField()
    seller=models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                               related_name="products"
                                )

    class Meta:
        #ordered by price
        ordering = ['price']
    def __str__(self):
        return self.name
