from django.db import models

# Create your models here.
class video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')
    description = models.CharField(max_length=400, null=True)

class comments(models.Model):
    visitorspost = models.ForeignKey(video, related_name='comment', on_delete=models.CASCADE, null=True)
    visitorscomment = models.CharField(max_length=275, null=True)