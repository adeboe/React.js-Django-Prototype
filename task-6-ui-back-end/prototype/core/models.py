#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Governs the models used by the web application. Also makes it easier
# to incorporate React.js to the overall project. 
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
#
# @author   Allan DeBoe
# @date     October 7th, 2022
# @since    October 2nd, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Create your models here.
class React(models.Model):
    description = models.CharField(max_length=2048)
    condition = models.CharField(max_length=256)