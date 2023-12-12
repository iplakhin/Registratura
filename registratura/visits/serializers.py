from rest_framework import serializers
from .models import Visit, Doctor, Device


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visit_date_time', 'message_text', 'rent_days', 'price', 'doctor', 'device')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("name", "telegram_id")


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("title", "number")
