from rest_framework import serializers
from terminosCondiciones.models import TerminosCondiciones


class TerminosCondicionesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TerminosCondiciones
        fields = ['title','content']