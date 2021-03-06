from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

#渲染登录界面
def toLogin(request):
    return render(request,'login.html')


#处理登录功能
def Login(request):

    #接收请求参数

    username = request.POST.get('username','')
    pwd = request.POST.get('pwd','')

    xxx=0
    if xxx==0:
        if username and pwd:
            num = QcwywebUserinfo.objects.filter(username = username,userpwd = pwd).count()
            if num >= 1:
                xxx=1
                return render(request, 'index.html')
            else:
                return HttpResponse('账号密码错误！')
        else:
            return HttpResponse('请输入正确的账号和密码！')
    else:
        xxx=1

def toquanguo(request):
    return render(request,'quanguo.html')


def todiqu(request):
    return render(request,'diqu.html')


def beijing(request):
    return render(request,'beijing.html')

def shanghai(request):
    return render(request,'shanghai.html')

def guangzhou(request):
    return render(request,'guangzhou.html')

def shenzhen(request):
    return render(request,'shenzhen.html')

def tianjin(request):
    return render(request,'tianjin.html')

def chongqing(request):
    return render(request,'chongqing.html')

def neimenggu(request):
    return render(request,'neimenggu.html')

def guangxi(request):
    return render(request,'guangxi.html')

def xizang(request):
    return render(request,'xizang.html')

def ningxia(request):
    return render(request,'ningxia.html')



def hebei(request):
    return render(request,'hebei.html')

def xinjiang(request):
    return render(request,'xinjiang.html')

def shanxicu(request):
    return render(request,'shanxicu.html')

def liaoning(request):
    return render(request,'liaoning.html')

def jilin(request):
    return render(request,'jilin.html')

def heilongjiang(request):
    return render(request,'heilongjiang.html')
def jiangsu(request):
    return render(request,'jiangsu.html')

def zhejiang(request):
    return render(request,'zhejiang.html')

def anhui(request):
    return render(request,'anhui.html')

def fujian(request):
    return render(request,'fujian.html')



def jiangxi(request):
    return render(request,'jiangxi.html')

def shandong(request):
    return render(request,'shandong.html')

def henan(request):
    return render(request,'henan.html')

def hubei(request):
    return render(request,'hubei.html')

def hunan(request):
    return render(request,'hunan.html')

def guangdong(request):
    return render(request,'guangdong.html')
def hainan(request):
    return render(request,'hainan.html')

def sichuan(request):
    return render(request,'sichuan.html')

def guizhou(request):
    return render(request,'guizhou.html')

def yunnan(request):
    return render(request,'yunnan.html')



def shanxi(request):
    return render(request, 'shanxicu.html')

def gansu(request):
    return render(request,'gansu.html')

def qinghai(request):
    return render(request,'qinghai.html')




def quanguo_1(request):
    return render(request,'中国各地区岗位数量分布地图.html')
def quanguo_2(request):
    return render(request,'中国各地区岗位数量条形图.html')
def quanguo_3(request):
    return render(request,'中国各工资占比饼图.html')
def quanguo_4(request):
    return render(request,'中国各地区高等教育岗位数量分布地图.html')
def quanguo_5(request):
    return render(request,'中国各地区普通教育岗位数量分布地图.html')


#渲染注册界面
# def toRegister(request):
#     return render(request,'register.html')

#处理注册功能
# def register(request):
#     username = request.POST.get('username', '')
#     pwd = request.POST.get('pwd', '')
#     if username and pwd:
#         user = QcwywebUserinfo(username = username,userpwd = pwd)
#         user.save()
#         return HttpResponse('注册成功！')
#     else:
#         return HttpResponse('请输入完整的账号和密码')

