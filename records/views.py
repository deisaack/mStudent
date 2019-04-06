import decorator
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status

from records.models import Student
from . import serializers as sz

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


@api_view(http_method_names=['post'])
def login(request):
    serializer = sz.LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"error": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
    data = serializer.data
    user = get_object_or_404(User, username=data['username'])
    if not user.check_password(data['password']):
        return Response({
            "error": "check your username or password"
        }, status=status.HTTP_400_BAD_REQUEST)
    adm_no = data['username'].replace('-', '/')
    try:
        student = Student.objects.get(adm_no=adm_no)
    except Student.DoesNotExist:
        return Response({
            "error": "Invalid Student"
        }, status.HTTP_404_NOT_FOUND)

    resp = {
        "user": sz.UserSerializer(user).data,
        "student": sz.StudentSerializer(student).data,
        "payments": sz.PaymentSerialier(student.payments, many=True).data,
        "primary_exams": sz.PrimaryExamSerializer(student.primary_exams, many=True).data,
        "secondary_exams": sz.SecondaryExamSerializer(student.secondary_exams, many=True).data,
        "university_exams": sz.UniversityExamSerializer(student.university_exams, many=True).data,
        "certificates": sz.CertificatesSerializer(student.certificates, many=True).data,
    }

    return Response(resp)


@api_view()
def get_student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({
            "error": "Invalid Student"
        }, status.HTTP_404_NOT_FOUND)

    resp = {
        "student": sz.StudentSerializer(student).data,
        "payments": sz.PaymentSerialier(student.payments, many=True).data,
        "primary_exams": sz.PrimaryExamSerializer(student.primary_exams, many=True).data,
        "secondary_exams": sz.SecondaryExamSerializer(student.secondary_exams, many=True).data,
        "university_exams": sz.UniversityExamSerializer(student.university_exams, many=True).data,
        "certificates": sz.CertificatesSerializer(student.certificates, many=True).data,
    }

    return Response(resp)
