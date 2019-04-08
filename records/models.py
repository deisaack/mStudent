from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    PRIMARY = "P"
    SECONDARY = "S"
    TERTIARY = "T"
    type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    adm_no = models.CharField(max_length=50, blank=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.adm_no + " " + self.full_name


class Teacher(models.Model):
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    reg_no = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.reg_no + " " + self.full_name


class PrimaryExam(models.Model):
    maths = models.PositiveIntegerField(null=True, blank=True)
    english = models.PositiveIntegerField(null=True, blank=True)
    kiswahili = models.PositiveIntegerField(null=True, blank=True)
    science = models.PositiveIntegerField(null=True, blank=True)
    sst = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    student = models.ForeignKey(Student, null=True, related_name='primary_exams', blank=True, on_delete=models.CASCADE)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)
    klass = models.CharField("Class", max_length=10, blank=True)

    @property
    def totalscore(self):
        try:
            return self.maths + self.english + self.kiswahili + self.science + self.sst
        except:
            return 0

    @property
    def average(self):
        try:
            return self.totalscore / 5
        except:
            return 0

    def __str__(self):
        return str(self.totalscore)

    @property
    def student_name(self):
        return self.student.full_name


class SecondaryExam(models.Model):
    maths = models.PositiveIntegerField(default=0)
    english = models.PositiveIntegerField(default=0)
    kiswahili = models.PositiveIntegerField(default=0)
    chem = models.PositiveIntegerField(default=0)
    phy = models.PositiveIntegerField(default=0)
    bio = models.PositiveIntegerField(default=0)
    comp = models.PositiveIntegerField(default=0)
    bst = models.PositiveIntegerField(default=0)
    agr = models.PositiveIntegerField(default=0)
    art = models.PositiveIntegerField(default=0)
    cre = models.PositiveIntegerField(default=0)
    music = models.PositiveIntegerField(default=0)
    date = models.DateField(blank=True, null=True)
    student = models.ForeignKey(Student, null=True, blank=True, related_name='secondary_exams', on_delete=models.CASCADE)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)
    klass = models.CharField("Class", max_length=10, blank=True)


    @property
    def totalscore(self):

        try:
            return self.maths + self.english + self.kiswahili + self.chem + self.chem + self.phy + self.bio + self.comp + \
                   self.bst + self.agr + self.art + self.cre + self.music
        except:
            return 0

    @property
    def average(self):
        return self.totalscore / 10

    def __str__(self):
        return str(self.totalscore)


class UniversityExam(models.Model):
    course_code = models.CharField(max_length=20, null=True, blank=True)
    course_name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now=False, blank=True, null=True)
    marks = models.PositiveIntegerField(null=True, blank=True)
    student = models.ForeignKey(Student, null=True, blank=True, related_name='university_exams', on_delete=models.CASCADE)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_code


class Certificate(models.Model):
    date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    student = models.ForeignKey(Student, null=True, blank=True, related_name='certificates', on_delete=models.CASCADE)
    score = models.CharField(max_length=50, blank=True)
    file = models.ImageField(upload_to="certificates", blank=True, null=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, null=True, blank=True, related_name='payments', on_delete=models.CASCADE)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    receipt_no = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.amount)

    @property
    def amount_paid(self):
        return f"KES. {self.amount}"
