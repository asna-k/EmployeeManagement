from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Salary must be greater than 0"
            )
        return value