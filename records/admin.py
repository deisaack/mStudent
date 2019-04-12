from django.contrib import admin

# Register your models here.
from records.models import Student, School, Teacher, PrimaryExam, UniversityExam, Certificate, SecondaryExam, Payment


class SchoolAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'type',
    )

    list_display = (
        'name',
        'type',
    )

    readonly_fields = (
        'name',
        'type',
    )


admin.site.register(School, SchoolAdmin)


class TeacherAdmin(admin.ModelAdmin):
    fields = (
        'school',
        'full_name',
        'reg_no',
    )

    readonly_fields = (
        'school',
        'full_name',
        'reg_no',
    )


admin.site.register(Teacher, TeacherAdmin)


class PrimaryExamAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'maths',
        'english',
        'kiswahili',
        'science',
        'sst',
        'totalscore',
        'average',
    )

    readonly_fields = (
        'student_name',
        'maths',
        'english',
        'kiswahili',
        'science',
        'sst',
        'totalscore',
        'average',
        'school',
        'student'
    )
    fields = (
        'student_name',
        'maths',
        'english',
        'kiswahili',
        'science',
        'sst',
        'totalscore',
        'average',
        'school',
    )


admin.site.register(PrimaryExam, PrimaryExamAdmin)


class UniversityExamAdmin(admin.ModelAdmin):
    fields = (
        'course_code',
        'course_name',
        'date',
        'marks',
        'student',
        'school',
    )

    readonly_fields = (
        'course_code',
        'course_name',
        'date',
        'marks',
        'student',
        'school',
    )

    list_display = (
        'student',
        'course_code',
        'course_name',
        'date',
        'marks',
    )

    search_fields = (
        'student__full_name',
    )


admin.site.register(UniversityExam, UniversityExamAdmin)


class CertAdmin(admin.ModelAdmin):
    fields = (
        'student',
        'name',
        'score',
        'date',
    )

    readonly_fields = (
        'student',
        'name',
        'score',
        'date',
    )

    list_display = (
        'student',
        'name',
        'score',
        'date',
    )

    search_fields = (
        'student__full_name',
    )


admin.site.register(Certificate, CertAdmin)
admin.site.register(SecondaryExam)


class PaymentAdmin(admin.ModelAdmin):
    fields = (
        'receipt_no',
        'amount',
        'date',
        'student',
        'school',
    )

    list_display = (
        'student',
        'school',
        'receipt_no',
        'date',
        'amount',
    )

    readonly_fields = (
        'student',
        'school',
        'receipt_no',
        'date',
        'amount',
    )

    search_fields = (
        'student',
        'receipt_no',

    )

    list_filter = (
        'school',
    )


admin.site.register(Payment, PaymentAdmin)


class PrimaryExamInline(admin.TabularInline):
    model = PrimaryExam
    # readonly_fields = ('totalscore', 'average',)
    readonly_fields = ('date', 'school', "klass", 'maths', 'english', 'kiswahili', 'science', 'sst', 'totalscore', 'average',)
    fields = ('date', 'school', "klass", 'maths', 'english', 'kiswahili', 'science', 'sst', 'totalscore', 'average',)
    extra = 0


class SecondaryExamInline(admin.TabularInline):
    model = SecondaryExam
    # readonly_fields = ('totalscore', 'average',)
    readonly_fields = ('school', 'date', "klass", 'maths', 'english', 'kiswahili', 'chem', 'phy', 'bio', 'comp', 'cre', 'totalscore', 'average',)
    fields = ('school', 'date', "klass", 'maths', 'english', 'kiswahili', 'chem', 'phy', 'bio', 'comp', 'cre', 'totalscore', 'average',)
    extra = 0


class UniversityExamInline(admin.TabularInline):
    model = UniversityExam
    readonly_fields = ('date', 'course_code', 'course_name', 'marks',)
    fields = ('date', 'course_code', 'course_name', 'marks',)
    extra = 0


class CertificateInline(admin.TabularInline):
    model = Certificate
    readonly_fields = (
        'student',
        'name',
        'score',
        'date',
        'file',
    )
    fields = (
        'student',
        'name',
        'score',
        'date',
        'file',
    )
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0
    readonly_fields = (
        'student',
        'school',
        'receipt_no',
        'date',
        'amount_paid',
    )

    fields = (
        'student',
        'school',
        'receipt_no',
        'date',
        'amount_paid',
        "amount"
    )


class StudentAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (
    #         None,
    #         {
    #             'fields': ('location', 'date',)
    #         }
    #     ),
    # )

    inlines = (PrimaryExamInline, SecondaryExamInline, UniversityExamInline, PaymentInline, CertificateInline)
    fields = (
        'adm_no',
        'full_name',
        'dob',
        'gender',
        'school',

    )

    readonly_fields = (
        'adm_no',
        'full_name',
        'dob',
        'gender',
        'school',

    )

    list_display = (
        'adm_no',
        'full_name',
        'dob',
        'gender',
        'school',

    )

    search_fields = (
        'admn_no',
        'full_name',
    )

    list_filter = (
        'school',
    )


admin.site.register(Student, StudentAdmin)
