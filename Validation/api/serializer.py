from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        #instance - old data from database
        print(instance)
        print(instance.name) #old name from database
        instance.name = validate_data.get('name', instance.name)
        print(instance.name) #updated name
        instance.roll = validate_data.get('roll', instance.roll) 
        instance.city = validate_data.get('city', instance.city) 
        instance.save()
        return instance
    
    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'sushma' and ct.lower() != 'shimoga':
            raise serializers.ValidationError('City must be Shimoga')
        return data