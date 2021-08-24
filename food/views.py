from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from . import models
# Create your views here.


class ChartView(APIView):
    def get(self,request):
        food_data = models.Food.objects.all()

        food_names = []
        food_values = []
        for x in food_data:
            food_names.append(x.name)
            food_values.append(x.value)

        json_data = {
            'names':food_names,
            'values':food_values,
        }

        

        return Response(json_data)