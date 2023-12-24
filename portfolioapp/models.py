from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    mobile_no = models.IntegerField()
    message = models.TextField()
