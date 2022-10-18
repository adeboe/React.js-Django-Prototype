#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deals with serializing data. Also makes it easier
# to incorporate React.js to the overall project. 
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
# https://stackoverflow.com/questions/31278418/django-rest-framework-custom-fields-validation
#
# @author   Allan DeBoe
# @date     October 17th, 2022
# @since    October 12th, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):

    class Meta:
        model = React
        fields = ['name','description','date_checked_in','date_checked_out','condition','location','check_out_by']

    def validate(self, data):
        if (data['date_checked_out'] < data['date_checked_in']):
            raise serializers.ValidationError("The patient cannot be checked out earlier than they are checked in!")
        elif (data['check_out_by'] < data['date_checked_in']):
            raise serializers.ValidationError("The patient cannot check out earlier than they are checked in!")
        else:
            return data