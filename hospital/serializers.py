from rest_framework import serializers
from .models import Register,Patient
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Register
        fields = ['id', 'name', 'role', 'department', 'password', 'confirmPassword']

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')  # Remove confirmPassword before saving
        validated_data['password'] = make_password(validated_data['password'])  # Encrypt the password
        return super().create(validated_data)


from .models import PharmacyStock
class PharmacyStockSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = PharmacyStock
        fields = '__all__'


from .models import HSNCode
class HSNCodeSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = HSNCode
        fields = '__all__'


from .models import Ventor
class VentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventor
        fields = ['id', 'ventor_name', 'phone', 'address', 'gst_number']


class PatientSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'


from .models import Doctor
class DoctorSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Doctor
        fields = '__all__'


from .models import CTReport
class CTReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTReport
        fields = ['age', 'date', 'gender', 'impression', 'investigation', 'patientId', 'patientName', 'approve','approve_time']


from .models import MRIReport
class MRIReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MRIReport
        fields = ['patientId', 'patientName', 'age', 'gender', 'investigation', 'impression', 'approve', 'approve_time']


from .models import Admission
class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'



from rest_framework import serializers
from .models import Summary
class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'


from .models import qrscan
class qrscanSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model =   qrscan
        fields = '__all__'