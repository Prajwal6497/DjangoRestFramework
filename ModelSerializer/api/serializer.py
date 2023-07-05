from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ('id','name', 'roll', 'city')
        # read_only_fields = ['name']
        # OR
        # extra_kwargs = {'name': {'read_only': True}}

    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value
    
    # Object Level Validation
    def validate(self, data):
        print(data)
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'adhira' and ct.lower() != 'shimoga':
            raise serializers.ValidationError('City must be Shimoga')
        return data



