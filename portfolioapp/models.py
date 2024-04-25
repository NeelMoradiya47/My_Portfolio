from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    mobile_no = models.IntegerField()
    message = models.TextField()

class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    url_link = models.CharField(max_length=255)
