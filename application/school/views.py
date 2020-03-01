from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import filters
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer, StudentDetailSerializer, StudentNestedSerializer
from .paginations import StandardResultsSetPagination


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class SchoolDetailViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = StandardResultsSetPagination


class StudentNestedViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentNestedSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

    def list(self, request, school_pk=None):
        queryset = self.filter_queryset(self.get_queryset()).filter(school=school_pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, school_pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['school'] = get_object_or_404(School.objects.all(), pk=school_pk)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None, school_pk=None):
        filter_kwargs = {
            'pk': pk,
            'school': school_pk
        }
        instance = get_object_or_404(self.queryset, **filter_kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer

