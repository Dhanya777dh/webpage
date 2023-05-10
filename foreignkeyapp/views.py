from django.shortcuts import render,redirect
from foreignkeyapp.models import Course,Student

# Create your views here.
def forfun(request):
    return render(request,'home.html')

def add_course(request):
    return render(request,'add_Course.html')
def addcourse_db(request):
    if request.method=='POST':
        coursename=request.POST.get('coursename')
        course_fee=request.POST.get('course_fee')
        course=Course(coursename=coursename,fee=course_fee)
        course.save()
        return redirect('/')

def add_student(request):
    courses=Course.objects.all()
    return render(request,'add_student.html',{'course':courses})
def addstudent_db(request):
    if request.method=='POST':
        name=request.POST['student_name']
        address=request.POST['student_address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=name,student_address=address,student_age=age,joining_date=jdate,course=course1) #m-v
        student.save()
        return redirect('/')

def show_details(request):
    student=Student.objects.all()
    return render(request,'showdetails.html',{'students':student})

def edit(request,pk):
    student=Student.objects.get(id=pk)
   
    course=Course.objects.all()
    return render(request,'edit.html',{'stud':student,'course':course})
    
def editdb(request,pk):
    if request.method=="POST":
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['name']
        student.student_address=request.POST['address']
        student.student_age=request.POST['age']
        student.joining_date=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student.course=course1
        student.save()
        return redirect('show_details')
    return render(request,'edit.html')

def delete(request,pk):
    student=Course.objects.get(id=pk)
    student.delete()
    return redirect('show_details')

