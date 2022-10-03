#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deals with serializing data. Also makes it easier
# to incorporate React.js to the overall project. 
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
#
# @author   Allan DeBoe
# @date     October 2nd, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['description','condition']