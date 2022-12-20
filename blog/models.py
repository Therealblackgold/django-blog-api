from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    body = RichTextField(blank=True, null=True)
    # description = RichTextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
