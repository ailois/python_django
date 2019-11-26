# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserMessage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def getform(requset):

    # 查询和条件查询
    # all_messages = UserMessage.objects.filter(name='ailois',address='上海')
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print(message.name)

    # 删除
    # all_message = UserMessage.objects.filter(object_id = '11111')
    # all_message = UserMessage.objects.filter(name = requset.POST.get('name',''))
    # all_message.delete()

    # for message in all_message:
    #     message.delete()

    # user_message = UserMessage()
    # user_message.name = 'ailois01'
    # user_message.email = 'ailois01@sina.com'
    # user_message.message = 'hello.ailois01'
    # user_message.address = '上海'
    # user_message.object_id = 'hello.ailois01'
    # user_message.save()

    # 通过表单进行新增
    # if requset.method == 'POST':
    #     name = requset.POST.get('name','')
    #     message = requset.POST.get('message','')
    #     address = requset.POST.get('address','')
    #     email = requset.POST.get('email','')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = '11111'
    #     user_message.message = message
    #     user_message.save()

    message = None
    all_message = UserMessage.objects.filter(name = 'ailois')
    # message = all_message[0]
    if all_message:
        message = all_message[0]
        # all_message.update(email = requset.POST.get('email',''),
        #                    address = requset.POST.get('address',''),
        #                    message = requset.POST.get('message',''))
        # all_message = UserMessage.objects.filter(name='ailois')
        # message = all_message[0]
    return render(requset,'留言板.html',{"my_message":message})

@csrf_exempt
def update(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message','')

    all_message = UserMessage.objects.filter(name='ailois')
    all_message.update(name=name,email=email,address=address,message=message)

    return HttpResponse()
    # return render(request, '留言板.html', {"my_message": message})