from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Track
from .serializers import TrackSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': 'all',
		'Search by Slack': '/?slack=slack_name',
		'Search by Track': '/?track=track',
	}

	return Response(api_urls)

    
@api_view(['GET'])
def view_items(request):
     
     
    # checking for the parameters from the URL
    if request.query_params:
        items = Track.objects.filter(**request.query_params.dict())
    else:
        items = Track.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = TrackSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
