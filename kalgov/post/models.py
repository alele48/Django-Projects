from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class PostJob(models.Model):

    title = models.CharField(max_length=200)

    text = models.CharField(max_length=600)

    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('postjob_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class FilesAdmin(models.Model):
    adminUpload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
