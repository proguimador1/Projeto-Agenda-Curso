from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'