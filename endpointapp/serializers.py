from django.db.models import fields
from rest_framework import serializers
from .models import Track



class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Track
		fields = ('slack', 'day', 'time', 'track', 'furl', 'repo', 'status')
		
