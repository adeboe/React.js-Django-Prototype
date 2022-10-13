#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Contains all of the views of the application
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
#
# @author   Allan DeBoe
# @date     October 12th, 2022
# @since    September 29th, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response # respooooooonse (I am losing brain cells)
from . models import *
from . serializer import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# View Class for React.js

class ReactView(APIView):

    serializer_class = ReactSerializer

    # Handles GET requests
    def get(self, request):
        data = [{
            'name': obj.name,
            'description': obj.description,
            'date_checked_in': obj.date_checked_in,
            'date_checked_out': obj.date_checked_out,
            'condition': obj.condition,
            'location': obj.location,
            'check_out_by': obj.check_out_by,
        } for obj in React.objects.all()]
        return Response(data)

    # Handles POST requests
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # Handles DELETE requests
    def delete(self, request):
        count = React.objects.all().delete()
        return JsonResponse({'message': 'the data was successfully deleted'})
