from django.db import models
from courses.models import Course

# Create your models here.


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    source_code_url = models.URLField(blank=True)  # Optional field for source code URL
    additional_resources = models.TextField(blank=True)  # Optional field for additional resources

    def __str__(self):
        return self.title

class SubModule(models.Model):
    module = models.ForeignKey(Module, related_name='submodules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    source_code_url = models.URLField(blank=True)  # Optional field for source code URL
    additional_resources = models.TextField(blank=True)  # Optional field for additional resources

    def __str__(self):
        return self.title