from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    item_name = models.CharField(max_length=30)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    votes = models.IntegerField()
    upload_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.item_name+": "+self.description

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})