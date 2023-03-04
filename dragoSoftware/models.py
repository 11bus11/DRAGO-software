from django.db import models

# Create your models here.
class Services( models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False, default="To be added")
    price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name