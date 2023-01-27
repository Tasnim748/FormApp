from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sector, Input

from .serializers import SectorSerializer, InputSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def getSectors(request):
    if request.method == 'GET':
        sectors = Sector.objects.all()
        serializer = SectorSerializer(sectors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("post request has come")
        body = request.data
        print(body)
        serializer = SectorSerializer(data=body, many=False)

        if serializer.is_valid():
            serializer.save()
            print('success')
            return Response("Note Added!")
        print('failure')
        return Response('Data is not valid')


@api_view(['GET', 'POST'])
def createInput(request):
    if request.method == 'GET':
        inputs = Input.objects.all()
        serializer = InputSerializer(inputs, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        body = request.data
        if body:
            input, created = Input.objects.get_or_create(username=body['username'])
            
            if created:
                for sector in body['sectors']:
                    input.sectors.add(Sector.objects.get(name=sector['name']))
                return HttpResponse('Your input submitted successfully')
            else:
                input.sectors.clear()
                for sector in body['sectors']:
                    input.sectors.add(Sector.objects.get(name=sector['name']))
                return HttpResponse('You have edited your submission successfully')
        else:
            return Response('request has no body!')
        