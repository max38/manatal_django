from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        if self.Meta.model.objects.filter(school=validated_data['school']).count() >= validated_data['school'].maximum_student:
            raise ValidationError("Maximum number ({}) of student reached in {}".format(
                validated_data['school'].maximum_student, validated_data['school'].name
            ))

        return super(StudentSerializer, self).create(validated_data)

    class Meta:
        model = Student
        fields = "__all__"


class StudentNestedSerializer(StudentSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(StudentSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Student
        fields = "__all__"
