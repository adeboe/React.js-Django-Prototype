#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Governs the models used by the web application. Also makes it easier
# to incorporate React.js to the overall project. 
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
# https://www.bezkoder.com/django-rest-api/
#
# @author   Allan DeBoe
# @date     October 15th, 2022
# @since    October 2nd, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.utils import timezone

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=64, blank=False, default='') 
    description = models.TextField()
    date_checked_in = models.DateField(default=timezone.now)
    date_checked_out = models.DateField()
    condition = models.CharField(max_length=256, blank=False, default='')
    location = models.CharField(max_length=256, blank=True, default='')
    check_out_by = models.DateField()