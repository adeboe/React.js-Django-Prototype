#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Governs the models used by the web application. Also makes it easier
# to incorporate React.js to the overall project. 
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
# https://www.bezkoder.com/django-rest-api/
#
# @author   Allan DeBoe
# @date     October 12th, 2022
# @since    October 2nd, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Create your models here.
class React(models.Model):
    name = models.CharField(max_length=64, blank=False, default='') 
    description = models.CharField(max_length=2048, blank=False, default='')
    date_checked_in = models.CharField(max_length=10, blank=True, default='mm/dd/yyyy')
    date_checked_out = models.CharField(max_length=10, blank=True, default='mm/dd/yyyy')
    condition = models.CharField(max_length=256, blank=False, default='')
    location = models.CharField(max_length=256, blank=True, default='')
    check_out_by = models.CharField(max_length=10, blank=True, default='mm/dd/yyyy')