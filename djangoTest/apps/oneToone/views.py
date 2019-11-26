from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt

from .models import userInfo,usertype
# Create your views here.

def getUser(requset):
    users = userInfo.objects.all()
    # print(users.all().count())
    if users:
        user = users[0]
    # print(user.user_type.name)
    return render(requset,'OneToOne.html',{'user':user,'users':users})

@csrf_exempt
def update(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')
        type = request.POST.get('type', '')
        users = userInfo.objects.filter(username = name)
        # users.update(username = name,password = password,email=email)
        if users:
            user = users[0]
            user.username = name
            user.email = email
            user.password = password
            userType = usertype()
            userType.name = type
            userType.save()
            user.user_type = userType
            user.save()

    # print(name,password,email,sep=',')
    return HttpResponse()

@csrf_exempt
def delete(request):
    if request == 'GET':
        username = request.GET.get('name')
        userInfo.delete(username = username)
    return HttpResponse()

# 表单提交
def insert(request):
    # print(request.method)
    # print(request.path)
    if request.method == 'POST':
        name = request.POST.get('name','')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        type = request.POST.get('type','')
        # print(name,password,email,type,sep=' ')
        user1 = userInfo()
        user1.username = name
        user1.password = password
        user1.email = email
        userType = usertype()
        userType.name = type
        userType.save()
        user1.user_type = userType
        user1.save()

    return redirect("http://127.0.0.1:8000/主外键Demo/show")




