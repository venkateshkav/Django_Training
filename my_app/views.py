from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse

# # Create your views here.

# def html_view(request):
#     # if request.method=="GET":
#     #     name = request.GET.get("username")
#     #     mail = request.GET.get("mail")
#     #     print(name,mail)
#     print(request.method)
#     if request.method=="POST":
#         name = request.POST.get("username")
#         mail = request.POST.get("mail")
#         print(name,mail)
#         return render(request,"index.html",{"name":name,"mail":mail})
#     return render(request,"index.html")

# #------------------------------------------------------------------------------>
# def session_data(request):
#     request.session["info"] = {
#         "name":"venkat",
#         "mail":"venkat@gmail.com",
#         "age":20
#     }
#     request.session["edu"] = {
#         "skill":"python",
#         "deg":"B.sc"
#     }
#     return render(request,"session.html")

# def get_session(request):
#     user_ifo = request.session.get("info",{})

#     # print(user_ifo["name"])
#     # return HttpResponse(user_ifo)
#     return render(request,"session2.html",{"info":user_ifo})

# def del_session(request):
#     # del request.session["info"]
#     request.session.flush()
#     # return HttpResponse("deleted")
#     return redirect("sessiondata")

from .models import *
def student_view(request):
    #orm queries
    # Student.objects.create(name="aadhi",age=20,mail="aadhi@gmail.com",course="full stack python",dob="2003-12-23",mobile="9087654321")
    student_data = Student.objects.all() 
    # print(student_data[0].age)
    # return HttpResponse("created")
    return render(request,"student.html",{"data":student_data})


    #  name = models.CharField()
    # age = models.IntegerField()
    # mail = models.EmailField(unique=True)
    # course=models.CharField()
    # dob=models.DateField()
    # mobile = models.CharField(max_length=12)
    # address= models.CharField(null=True,blank=True)


def student_delete(request,stu_id):
    st = Student.objects.get(id=stu_id)
    print(st)
    st.delete()
    return redirect("stu-forms")

def stuent_edit(request):
    st = Student.objects.get(id=3)
    st.age=22
    st.save()
    return redirect("student-add")

from .forms import StudentForm
def student_create(request,id=None):

    
    if id:
        stu = Student.objects.get(id=id)
        form = StudentForm(instance=stu)
        student_data = Student.objects.all()
    else:
        form = StudentForm()
        student_data = Student.objects.all()
    if request.method =="POST":
        if request.POST.get("action")=="create":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("stu-forms")
        elif request.POST.get("action")=="edit":
            stu = Student.objects.get(id=id)
            form = StudentForm(instance=stu,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect("stu-forms")

    return render(request,"student.html",{"form":form,"data":student_data})

def student_update(request):
    st = Student.objects.get(id=3)
    form = StudentForm(instance=st)
    if request.method=="POST":
        form = StudentForm(instance=st,data=request.POST)
        if form.is_valid():
            form.save()
    return render(request,"student_edit.html",{"form":form})

from .forms import *

def product_view(request):
    form = ProdctForm()
    data = Products.objects.all()
    # print(data[7].category_name.created_at)
    if request.method == "POST":        
        form = ProdctForm(request.POST)
        if form.is_valid():
            form.save() 
        else:
            return HttpResponse("error occured")
    return render(request,"product.html",{"form":form,"data":data})


def pro_edit(request,pro_id):
    pro = Products.objects.get(id=pro_id)
    form = ProdctForm(instance=pro)
    if request.method == "POST":
        form = ProdctForm(instance=pro, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("pro-create")
    return render(request,"pro_edit.html",{"form":form})


def product_query(request):
    data = Products.objects.filter(stock__gt=20)
    data= Products.objects.filter(price__lt=500)
    asc_order = Student.objects.order_by("-dob").first()
    asc_order = Student.objects.filter(course="java").first()
    asc_order= Student.objects.values("name","course")
    asc_order = Student.objects.values_list("course").distinct()
    

    print(asc_order)
    return HttpResponse(asc_order)

from django.db.models import Sum,Count,Min,Max,Avg
from django.db.models import Q, F

def orm_view(request):
    data = Student.objects.aggregate(sum_age=Avg('age'))
    print(data)
    data = Student.objects.values('course').annotate(sum_age=Count("id"))
    data = Student.objects.filter(Q(course="python") & Q(age=22))
    data = Products.objects.annotate(total= F("price")*F("stock"))
    data = Products.objects.filter(price__lt=F("stock"))
    print(data)
    # for i in data:
    #     print(i.total)
    
    return HttpResponse(data)


# def product_view(request):
#     pro = Products.objects.all()
#     print(pro)


def image_view(request):
    img = ImageModel.objects.all()
    print(img[0].image)
    return render(request,"index.html",{'data':img})

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def student_getall(request):
    std = Student.objects.values()
    print(std)
    return JsonResponse(list(std),safe=False)


from rest_framework.views import APIView
from .serializers import *


class StudentView(APIView):
    def get(self,request):
        std = Student.objects.all()
        std_serial = StudentSerializer(std,many=True)
        return Response(std_serial.data)
 

    def post(self,request):
        std = StudentSerializer(data=request.data)
        if std.is_valid():
            std.save()
            return Response({"msg":"data saved","data":std.data})
        else:
            return Response({"error":std.errors})