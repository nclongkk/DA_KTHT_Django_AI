from rest_framework import  serializers
from FacerecogApp.models import Timecheckin

class TimecheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model=Timecheckin
        fields=('group','user','day','timeLate')