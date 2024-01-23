from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Empregistration,Salaryprocess, Patientsignup,Admissionform, Opdappoientment


curl = settings.CURRENT_URL


def Index(request):
    return render(request, "index.html")

def About_us(request):
    return render(request, "about_us.html", {"curl":curl})

def Service(request):
    return render(request, "services.html", {"curl":curl})

def Blog(request):
    return render(request, "blog.html",{"curl":curl})

def Gallary(request):
    return render(request, "gallery.html", {"curl":curl})

def Contact(request):
    return render(request, "contact_us.html", {"curl":curl})

def Login(request):
    return render(request, "login.html", {"curl":curl})

def Accounts(request):
    return render(request, "accounts.html", {"curl":curl})

def Employeesrc(request):
    return render(request, "employeesrc.html", {"curl":curl})

def Salary(request):
    if request.method == "POST":
        NWD= request.POST["NWD"]
        PL= request.POST["PL"]
        CL= request.POST["CL"]
        Accountnumber= request.POST["Accountnumber"]
        IFSC= request.POST["IFSC"]
        Basicsalary = request.POST["Basicsalary"]
        TD= request.POST["TD"]
        PF= request.POST["PF"]
        HRA= request.POST["HRA"]
        Grosssaray = request.POST["Grosssaray"]
        Netsalary = request.POST["Netsalary"]
        Date = request.POST["Date"]

        print(NWD,PL,CL,Accountnumber,IFSC,Basicsalary,TD,PF,HRA,Grosssaray ,Netsalary,Date)
        # SalaryObj = Salaryprocess(NWD=NWD,PL=PL,CL=CL,Accountnumber=Accountnumber,IFSC=IFSC,Basicsalary=Basicsalary,TD=TD,HRA=HRA,
        #                          Grosssaray=Grosssaray,Netsalary=Netsalary,Date=Date )

        msg=""
        try:
            # PatientSignupObj.save()
            msg="Salary Details Summited Successfully"
        except:
            msg="User Not Register"    
        return render(request,"petientsignup.html",{'curl':curl})
    else:
        return render(request,"petientsignup.html",{'curl':curl})

       
    return render(request, "salary.html", {"curl":curl})

def Reception(request):
        return render(request, "reception.html",{"curl":curl})

def Appointment(request):
    return render(request,"appointment.html",{"curl":curl})

def Addmissionform(request):
    return render(request, "addmissionform.html",{"curl":curl})

def Discharge(request):
    return render(request,"discharge.html",{"curl":curl})

def Hospitaladmin(request):
    return render(request,"hospitaladmin.html", {'curl':curl})

def Temporary(request):
    return render(request,"temporary.html",{"curl": curl})

def Registration(request):
    if request.method == "POST":
        EmpFirstname = request.POST["EmpFirstname"]
        EmpLastname = request.POST["EmpLastname"]
        EmpEmployeeid = request.POST["EmpEmployeeid"]
        EmpEmail = request.POST["EmpEmail"]
        EmpPassword = request.POST["EmpPassword"]
        EmpMobileno = request.POST["EmpMobileno"]
        EmpAdhar = request.POST["EmpAdhar"]
        EmpPAN = request.POST["EmpPAN"]
        EmpUAN= request.POST["EmpUAN"]
        EmpGender = request.POST["EmpGender"]
        EmpDOB = request.POST["EmpDOB"]
        EmpDOJ = request.POST["EmpDOJ"]
        EmpTOE = request.POST["EmpTOE"]
        EmpROE = request.POST["EmpROE"]
        EmpDesignation = request.POST["EmpDesignation"]
        EmpPhoto = request.POST["EmpPhoto"]
        EmpDocument= request.POST["EmpDocument"]
        EmpDocument = request.POST["EmpDocument"]
        EmpRletter = request.POST["EmpRletter"]
        EmpAcadmic = request.POST["EmpAcadmic"]
        EmpEletter = request.POST["EmpEletter"]
        EmpPhospital = request.POST["EmpPhospital"]
        EmpCaddress = request.POST["EmpCaddress"]
        EmpDate = request.POST["EmpDate"]
        EmpStatus = request.POST["EmpStatus"]
        CurrentTime = request.POST["CurrentTime"]
        
        print(EmpFirstname,EmpLastname,EmpEmployeeid,EmpEmail,EmpPassword,EmpMobileno,EmpAdhar,EmpPAN,EmpUAN,EmpGender,EmpDOB,
              EmpDOJ,EmpTOE,EmpROE,EmpDesignation,EmpPhoto,EmpDocument,EmpRletter,EmpAcadmic,EmpEletter,EmpPhospital,
              EmpCaddress,EmpDate,EmpStatus,CurrentTime)
        
        # RegObj = Empregistration (EmpFirstname=EmpFirstname,EmpLastname=EmpLastname,EmpEmployeeid=EmpEmployeeid,
        # EmpEmail=EmpEmail,EmpPassword=EmpPassword,EmpMobileno=EmpMobileno,EmpAdhar=EmpAdhar,EmpPAN=EmpPAN,EmpUAN=EmpUAN,
        # EmpGender=EmpGender,EEmpDOB=EmpDOB,EmpDOJ=EmpDOJ,EmpTOE=EmpTOE,EmpROE=EmpROE,EmpDesignation=EmpDesignation,
        # EmpPhoto=EmpPhoto,EmpDocument=EmpDocument,EmpRletter=EmpRletter,EmpAcadmic=EmpAcadmic,EmpEletter=EmpEletter,
        # EmpPhospital=EmpPhospital,EmpCaddress=EmpCaddress,EmpDate=EmpDate,EmpStatus=EmpStatus,CurrentTime=CurrentTime)

    return render(request,"registration.html",{"curl":curl})

def Updateemployee(request):
    return render(request,"updateemployee.html",{'curl':curl})

def Petientsignup(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Email = request.POST["Email"]
        Number = request.POST["Number"]
        Password = request.POST["Password"]
        Address = request.POST["Address"]
        Gender = request.POST["Gender"]
        DOB  = request.POST["DOB"]
        
        # PatientSignupObj=Patientsignup(Name=Name,Email=Email,Number=Number,password=Password,Address=Address,Gender=Gender,DOB=DOB)
        msg=""
        try:
            print(Name,Email,Number,Password,Address,Gender,DOB)
            # PatientSignupObj.save()
            msg="User Register Successfully"
        except:
            msg="User Not Register"    
        return render(request,"petientsignup.html",{'curl':curl})
    else:
        return render(request,"petientsignup.html",{'curl':curl})


def ipdpatienprescription(request):
    return render(request,"ipdpatienprescription.html", {'curl':curl}) 

def Ipdprescriptiondetails(request):
    return render(request, "ipdprescriptiondetails.html",{'curl':curl})

def Opdpatienprescription(request):
    return render(request,"opdpatienprescription.html",{'curl':curl})

def Opdprescriptiondetails(request):
    return render(request,"opdprescriptiondetails.html",{'curl':curl})

def Salarysrc(request):
    return render(request,"salarysrc.html", {'curl':curl})

def Equipements(request):
    return render(request,"equipements.html",{'curl':curl})