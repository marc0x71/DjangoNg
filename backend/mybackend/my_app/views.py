from django.http import JsonResponse
from django.shortcuts import render

from my_app.models import ExampleModel
from my_app.serializers import ExampleModelSerializer


def get_data(request):
	data = ExampleModel.objects.all()
	if request.method == 'GET':
		serializer = ExampleModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
