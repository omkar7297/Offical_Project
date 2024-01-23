from django.db import models
from django.utils import timezone


class Empregistration(models.Model):
    EmpFirstname = models.CharField(max_length=50)
    EmpLastname = models.CharField(max_length=50)
    EmpEmployeeid = models.CharField(max_length=20,unique=True)
    EmpEmail = models.CharField(max_length=100,unique=True)
    EmpPassword = models.CharField(max_length=50) 
    EmpMobileno = models.CharField(max_length=100)
    EmpAdhar = models.CharField(max_length = 100,unique=True)
    EmpPAN = models.CharField(max_length=20,unique=True)
    EmpUAN = models.CharField(max_length = 20)
    EmpGender = models.CharField(max_length = 50)
    EmpDOB = models.DateField(max_length=10)
    EmpDOJ = models.CharField(max_length=100)
    EmpTOE = models.CharField(max_length=100)
    EmpROE = models.CharField(max_length=100)
    EmpDesignation = models.CharField(max_length = 100)
    EmpPhoto = models.CharField(max_length=1000000)
    EmpDocument = models.CharField(max_length=1000000)
    EmpDesignation= models.CharField(max_length=100)
    EmpRletter = models.CharField(max_length=100)
    EmpAcadmic = models.CharField(max_length=100)
    EmpEletter = models.CharField(max_length=100)
    EmpPhospital = models.CharField(max_length = 100)
    EmpCaddress = models.CharField(max_length=100)
    EmpDate = models.DateTimeField('date published', default=timezone.now)
    EmpStatus = models.IntegerField(default=0)
    CurrentTime = models.TimeField(max_length = 100)

    def __str__(self):
        return "{0},{1}, {2}, {3}, {4}, {5}, {6}, {7}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {16}, {17}, {18}, {19}, {20}, {21}, {22},{23}".format(self.EmpFirstname,self.EmpLastname,self.Employeeid,self.EmpEmail,self.EmpPassword,self.EmpMobileno,self.EmpAdhar,self.EmpPAN,self.EmpUAN,self.EmpGender,self.EmpDOB,self.EmpDOJ,self.EmpTOE,self.EmpROE,self.EmpDesignation,self.EmpPhoto,self.EmpDocuments,self.EmpRletter,self.EmpAcadmic,self.EmpEletter,self.EmpPhospital,self.EmpCaddress,self.EmpDate,self.EmpStatus)


class Salaryprocess (models.Model):
    NWD= models.CharField(max_length=100)
    PL = models.CharField(max_length=100)
    CL= models.CharField(max_length=100)
    Accountnumber= models.CharField(max_length=100)
    IFSC= models.CharField(max_length=100)
    Basicsalary= models.CharField(max_length=100)
    TA= models.CharField(max_length=100)
    TD= models.CharField(max_length=100)
    HRA= models.CharField(max_length=100)
    PF= models.CharField(max_length=100)
    Grosssaray= models.CharField(max_length=100)
    Netsalary= models.CharField(max_length=100)
    Date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return "{0},{1}, {2}, {3}, {4}, {5}, {6}, {7}, {7}, {8}, {9}, {10}, {11}, {12}".format(self.NWD, self.PL,self.CL,self.Accountnumber,self.IFSC,self.Basicsalary,self.TA,self.TD,self.HRA,self.PF,self.Grosssaray,self.Netsalary,self.Date) 


class Patientsignup(models.Model):

    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Number = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    DOB = models.DateField()
    Date = models.DateTimeField('date published', default=timezone.now)

    def __srt__(self):
         return "{0},{1}, {2}, {3}, {4}, {5}, {6},".format(self.Name,self.Email,self.Number,self.Password,self.Address,self.Gender,self.DOB,self.Date)


class Admissionform(models.Model):

    Aname = models.CharField(max_length=100)
    Aguardian =models.CharField(max_length=100)
    Anumber =models.CharField(max_length=100)
    ADOB =models.CharField(max_length=100)
    Aaddress = models.CharField(max_length=100)
    Asex = models.CharField(max_length=100)
    Asickness = models.CharField(max_length=100)
    Aamount = models.CharField(max_length=10000000)
    Aadhar = models.CharField(max_length=100)
    Aayushman = models.CharField(max_length=100) 
    Apatientid = models.CharField(max_length=100)
    Adate = models.DateTimeField('date published', default=timezone.now)
    Treatment = models.CharField(max_length=1000)

    def __str__(self):

        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},".format(self.Aname,self.Aguardian,self.Anumber,self.ADOB,self.Aaddress,self.Asex,self.Asickness,self.Aamount,self.Aadhar,self.Aayushman,self.Apatientid,self.Adate,self.Treatment)


class Dischargeform(models.Model):
    #Inherit some value from Admissionform class 
    Aexaminerdoctor = models.CharField(max_length=100)
    Anodays = models.CharField(max_length=100)
    Ddate = models.DateTimeField('date published', default=timezone.now)
    Dprescription = models.CharField(max_length=1000)
    Dnote = models.CharField(max_length=1000)

    def __str__(self):

        return "{0},{1},{2},{3},{4},".format(self.Aexaminerdoctor,self.Anodays,self.Ddate,self.Dprescription,self.Dnote)


class Ipdprescription(models.Model):
    IPDPrescription = models.CharField(max_length=10000000)
    Date = models.DateTimeField('date published', default=timezone.now)
    Examinardoctor = models.CharField(max_length=100)

    def __str__(self):
    
      return "{0},{1},".format(self.IPDPrescription,self.Date)


class Opdprescription(models.Model):
    Patientprescription = models.CharField(max_length=1000000)
    Date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return "{0},{1},".format(self.Patientprescription,self.Date)


class Opdappoientment(models.Model):
    Patientname = models.CharField(max_length=100)
    Patientguardian = models.CharField(max_length=100)
    Patientnumber = models.CharField(max_length=100)
    PatientDOB = models.DateField(max_length=20)
    Patientaddress = models.CharField(max_length=100)
    Patientsex = models.CharField(max_length=100)
    Patientsickness = models.CharField(max_length=100)
    Patientappointdoctor = models.CharField(max_length=100)
    PatientTNo = models.CharField(max_length=100)
    PatientDate = models.DateTimeField('date published', default=timezone.now)
    PatientDP = models.CharField(max_length=100)
    
    def __str__(self):
         return "{0},{1}, {2}, {3}, {4}, {5}, {6}, {7}, {7}, {8}, {9}, {10},".format(self.Patientname, self.Patientguardian, self.Patientnumber, self.PatientDOB, self.Patientaddress, self.Patientsex,self.Patientsickness,self.Patientappointdoctor,self.PatientTNo,self.PatientDate,self.PatientDP)
    

class Equipements(models.Model):
    Equipementname = models.CharField(max_length=100)
    Equipementquantity = models.CharField(max_length=100)
    Equipementprice = models.CharField(max_length=100)

    def __str__(self):
        return "{0},{1},{2}".format(self.Equipementname,self.Equipementquantity,self.Equipementprice)
