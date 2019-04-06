from django.contrib.auth.models import User
from rest_framework import serializers

from records.models import Student, PrimaryExam, SecondaryExam, UniversityExam, Certificate, Payment


class StudentSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = (
            "id",
        "full_name",
        "adm_no",
        "dob",
        "gender",
        "school")

    def get_school(self, obj):
        return obj.school.name


class PrimaryExamSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()

    class Meta:
        model = PrimaryExam
        fields = "__all__"

    def get_school(self, obj):
        return obj.school.name

class SecondaryExamSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    class Meta:
        model = SecondaryExam
        fields = ("id",
            "maths",
            "english",
            "kiswahili",
            "chem",
            "phy",
            "bio",
            "comp",
            "bst",
            "agr",
            "art",
            "cre",
            "music",
            "date",
            "klass",
            "student",
            "school")

    def get_school(self, obj):
        return obj.school.name


class UniversityExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityExam
        fields = "__all__"


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'id',
        )


class PaymentSerialier(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ("id",
            "date",
            "amount",
            "receipt_no",
            "student",
            "school"
                  )
    def get_student(self, obj):
        return obj.student.full_name

    def school(self, obj):
        return obj.school.name

