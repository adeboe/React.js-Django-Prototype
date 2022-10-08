#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Contains all of the views of the application
#
# References:
# https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
#
# @author   Allan DeBoe
# @date     October 7th, 2022
# @since    September 29th, 2022
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.respoonse import Response
from . models import *
from . serializer import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# View Class for React.js

class ReactView(APIView):

    serializer_class = ReactSerializer

    # Handles GET requests
    def get(self, request):
        data = [ {
            'description': obj.description,
            'condition': obj.condition,
        } for obj in React.objects.all()]
        return Response(data)

    # Handles POST requests
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)