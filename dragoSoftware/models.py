from django.db import models

# Create your models here.
class Services(models.Model):
    class Meta:
        verbose_name = "Our Services"

    nr = models.IntegerField(null=False, blank=False, default=0)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False, default="To be added")
    price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['nr']


class AboutUs(models.Model):
    class Meta:
        verbose_name = "About Us"

    nr = models.IntegerField(null=False, blank=False, default=0)
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.CharField(max_length=2000, null=False, blank=False, default="To be added")
    image = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.nr)

    class Meta:
        ordering = ['nr']
