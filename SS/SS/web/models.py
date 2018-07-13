from django.db import models


# Create your models here.

class Info(models.Model):
    CSE = 'CSE'
    MC = 'MC'
    Departments = (
        ( CSE , 'CSE'),
        ( MC, 'MC'),
    )
    Name = models.CharField(max_length=250, help_text="Enter Name")
    Designation = models.CharField(max_length=300)
    Department = models.CharField(
        max_length=100,
        choices=Departments,
        default=CSE,
    )
    Phone = models.CharField(max_length=20)
    webmail = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    residence = models.CharField(max_length=250)
    # photo = models.FileField()

class Education(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    Degree = models.CharField(max_length=25)
    College_Name = models.CharField(max_length=250)


class Work(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    Position = models.CharField(max_length=200)
    Place=models.CharField(max_length=200)

class ContPhdstudents(models.Model):
    name = models.CharField(max_length=250)

class CompPhdstudents(models.Model):
    name = models.CharField(max_length=250)

class ContMTstudents(models.Model):
    name = models.CharField(max_length=250)

class ContBTstudents(models.Model):
    name = models.CharField(max_length=250)

class CompMTstudents(models.Model):
    name = models.CharField(max_length=250)

class CompBTstudents(models.Model):
    name = models.CharField(max_length=250)

class students(models.Model):
    cphd = models.ForeignKey(ContPhdstudents, on_delete=models.CASCADE)
    cophd = models.ForeignKey(CompPhdstudents, on_delete=models.CASCADE)
    cmt = models.ForeignKey(ContMTstudents, on_delete=models.CASCADE)
    cbt = models.ForeignKey(ContBTstudents, on_delete=models.CASCADE)
    comt = models.ForeignKey(CompMTstudents, on_delete=models.CASCADE)
    cobt = models.ForeignKey(CompBTstudents, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class publications(models.Model):
    pub = models.CharField(max_length=500)

class recognitions(models.Model):
    recg = models.CharField(max_length=500)

class project(models.Model):
    title = models.CharField(max_length=100)
    pi = models.CharField(max_length=10)
    agency = models.CharField(max_length=10)
    startyear = models.CharField(max_length=10)
    endyear = models.CharField(max_length=10)


class teaching(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        (2017-, '2017'),
        (2016-17, '2016'),
        (2015-16, '2015'),
        (2014-15, '2014'),
        (2013-14, '2013'),
        (2012-13,'2012'),
        (2011-12,'2011'),
        (2010-11,'2010'),
        (2009-10,'2009'),
        (2008-09,'2008'),

    )
    year = models.CharField(
        max_length=7,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=2017-,
    )
    SEMESTERS= (
        (odd, 'odd'),
        (even, 'even')
    )
    sem= models.CharField(
        max_length=4, choice=SEMESTERS, default=odd
    )
    course=models.CharField(max_length=500)


