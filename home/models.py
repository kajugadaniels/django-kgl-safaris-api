from django.db import models
from django.utils.text import slugify

class TourPackage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='tour-packages/', null=True, blank=True)
    number_of_people = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(TourPackage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title