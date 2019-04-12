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
    totalscore = serializers.SerializerMethodField()
    average = serializers.SerializerMethodField()

    class Meta:
        model = PrimaryExam
        fields = ("school", "average", "sst", "date", "klass", "student", "school",
                  "totalscore", "id", "maths", "english", "kiswahili", "science")

    def get_school(self, obj):
        return obj.school.name

    def get_totalscore(self, obj):
        return obj.totalscore

    def get_average(self, obj):
        return obj.average


class SecondaryExamSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    totalscore = serializers.SerializerMethodField()
    average = serializers.SerializerMethodField()

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
                  "school", "average",
                  "totalscore",)

    def get_school(self, obj):
        return obj.school.name

    def get_totalscore(self, obj):
        return obj.totalscore

    def get_average(self, obj):
        return obj.average


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
    school = serializers.SerializerMethodField()

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

    def get_school(self, obj):
        return obj.school.name
