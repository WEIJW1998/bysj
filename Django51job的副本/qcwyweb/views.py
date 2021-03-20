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
    return render(request, 'shanxi.html')

def gansu(request):
    return render(request,'gansu.html')

def qinghai(request):
    return render(request,'qinghai.html')




def quanguo_1(request):
    return render(request,'全国各地区岗位数量分布地图.html')
def quanguo_2(request):
    return render(request,'全国各地区岗位数量条形图.html')
def quanguo_11(request):
    return render(request,'全国各地区岗位数量折线图.html')
def quanguo_3(request):
    return render(request,'全国各工资占比饼图.html')
def quanguo_4(request):
    return render(request,'全国各地区高等教育岗位数量分布地图.html')
def quanguo_5(request):
    return render(request,'全国各地区普通教育岗位数量分布地图.html')

def quanguo_6(request):
    return render(request,'全国公司规模象型柱图.html')
def quanguo_7(request):
    return render(request,'全国经验要求漏斗图.html')
def quanguo_8(request):
    return render(request,'全国城市词云图.html')
def quanguo_9(request):
    return render(request,'全国公司待遇词云图.html')
def quanguo_10(request):
    return render(request,'全国热门行业词云图.html')

#----------------------------------------------------------------------------------------


def anhui_1(request):
    return render(request,'安徽岗位数量分布地图.html')
def anhui_2(request):
    return render(request,'安徽各工资占比饼图.html')
def anhui_3(request):
    return render(request,'安徽公司规模象型柱图.html')
def anhui_4(request):
    return render(request,'安徽经验要求漏斗图.html')
def anhui_5(request):
    return render(request,'安徽热门行业词云图.html')

def beijing_1(request):
    return render(request,'北京岗位数量分布地图.html')
def beijing_2(request):
    return render(request,'北京各工资占比饼图.html')
def beijing_3(request):
    return render(request,'北京公司规模象型柱图.html')
def beijing_4(request):
    return render(request,'北京经验要求漏斗图.html')
def beijing_5(request):
    return render(request,'北京热门行业词云图.html')

def chongqing_1(request):
    return render(request,'重庆岗位数量分布地图.html')
def chongqing_2(request):
    return render(request,'重庆各工资占比饼图.html')
def chongqing_3(request):
    return render(request,'重庆公司规模象型柱图.html')
def chongqing_4(request):
    return render(request,'重庆经验要求漏斗图.html')
def chongqing_5(request):
    return render(request,'重庆热门行业词云图.html')

def fujian_1(request):
    return render(request,'福建岗位数量分布地图.html')
def fujian_2(request):
    return render(request,'福建各工资占比饼图.html')
def fujian_3(request):
    return render(request,'福建公司规模象型柱图.html')
def fujian_4(request):
    return render(request,'福建经验要求漏斗图.html')
def fujian_5(request):
    return render(request,'福建热门行业词云图.html')

def gansu_1(request):
    return render(request,'甘肃岗位数量分布地图.html')
def gansu_2(request):
    return render(request,'甘肃各工资占比饼图.html')
def gansu_3(request):
    return render(request,'甘肃公司规模象型柱图.html')
def gansu_4(request):
    return render(request,'甘肃经验要求漏斗图.html')
def gansu_5(request):
    return render(request,'甘肃热门行业词云图.html')

def guangdong_1(request):
    return render(request,'广东岗位数量分布地图.html')
def guangdong_2(request):
    return render(request,'广东各工资占比饼图.html')
def guangdong_3(request):
    return render(request,'广东公司规模象型柱图.html')
def guangdong_4(request):
    return render(request,'广东经验要求漏斗图.html')
def guangdong_5(request):
    return render(request,'广东热门行业词云图.html')

def guangxi_1(request):
    return render(request,'广西岗位数量分布地图.html')
def guangxi_2(request):
    return render(request,'广西各工资占比饼图.html')
def guangxi_3(request):
    return render(request,'广西公司规模象型柱图.html')
def guangxi_4(request):
    return render(request,'广西经验要求漏斗图.html')
def guangxi_5(request):
    return render(request,'广西热门行业词云图.html')

def guangzhou_1(request):
    return render(request,'广州岗位数量分布地图.html')
def guangzhou_2(request):
    return render(request,'广州各工资占比饼图.html')
def guangzhou_3(request):
    return render(request,'广州公司规模象型柱图.html')
def guangzhou_4(request):
    return render(request,'广州经验要求漏斗图.html')
def guangzhou_5(request):
    return render(request,'广州热门行业词云图.html')

def guizhou_1(request):
    return render(request,'贵州岗位数量分布地图.html')
def guizhou_2(request):
    return render(request,'贵州各工资占比饼图.html')
def guizhou_3(request):
    return render(request,'贵州公司规模象型柱图.html')
def guizhou_4(request):
    return render(request,'贵州经验要求漏斗图.html')
def guizhou_5(request):
    return render(request,'贵州热门行业词云图.html')

def hainan_1(request):
    return render(request,'海南岗位数量分布地图.html')
def hainan_2(request):
    return render(request,'海南各工资占比饼图.html')
def hainan_3(request):
    return render(request,'海南公司规模象型柱图.html')
def hainan_4(request):
    return render(request,'海南经验要求漏斗图.html')
def hainan_5(request):
    return render(request,'海南热门行业词云图.html')

def hebei_1(request):
    return render(request,'河北岗位数量分布地图.html')
def hebei_2(request):
    return render(request,'河北各工资占比饼图.html')
def hebei_3(request):
    return render(request,'河北公司规模象型柱图.html')
def hebei_4(request):
    return render(request,'河北经验要求漏斗图.html')
def hebei_5(request):
    return render(request,'河北热门行业词云图.html')

def heilongjiang_1(request):
    return render(request,'黑龙江岗位数量分布地图.html')
def heilongjiang_2(request):
    return render(request,'黑龙江各工资占比饼图.html')
def heilongjiang_3(request):
    return render(request,'黑龙江公司规模象型柱图.html')
def heilongjiang_4(request):
    return render(request,'黑龙江经验要求漏斗图.html')
def heilongjiang_5(request):
    return render(request,'黑龙江热门行业词云图.html')

def henan_1(request):
    return render(request,'河南岗位数量分布地图.html')
def henan_2(request):
    return render(request,'河南各工资占比饼图.html')
def henan_3(request):
    return render(request,'河南公司规模象型柱图.html')
def henan_4(request):
    return render(request,'河南经验要求漏斗图.html')
def henan_5(request):
    return render(request,'河南热门行业词云图.html')

def hubei_1(request):
    return render(request,'湖北岗位数量分布地图.html')
def hubei_2(request):
    return render(request,'湖北各工资占比饼图.html')
def hubei_3(request):
    return render(request,'湖北公司规模象型柱图.html')
def hubei_4(request):
    return render(request,'湖北经验要求漏斗图.html')
def hubei_5(request):
    return render(request,'湖北热门行业词云图.html')

def hunan_1(request):
    return render(request,'湖南岗位数量分布地图.html')
def hunan_2(request):
    return render(request,'湖南各工资占比饼图.html')
def hunan_3(request):
    return render(request,'湖南公司规模象型柱图.html')
def hunan_4(request):
    return render(request,'湖南经验要求漏斗图.html')
def hunan_5(request):
    return render(request,'湖南热门行业词云图.html')

def jiangsu_1(request):
    return render(request,'江苏岗位数量分布地图.html')
def jiangsu_2(request):
    return render(request,'江苏各工资占比饼图.html')
def jiangsu_3(request):
    return render(request,'江苏公司规模象型柱图.html')
def jiangsu_4(request):
    return render(request,'江苏经验要求漏斗图.html')
def jiangsu_5(request):
    return render(request,'江苏热门行业词云图.html')

def jiangxi_1(request):
    return render(request,'江西岗位数量分布地图.html')
def jiangxi_2(request):
    return render(request,'江西各工资占比饼图.html')
def jiangxi_3(request):
    return render(request,'江西公司规模象型柱图.html')
def jiangxi_4(request):
    return render(request,'江西经验要求漏斗图.html')
def jiangxi_5(request):
    return render(request,'江西热门行业词云图.html')

def jilin_1(request):
    return render(request,'吉林岗位数量分布地图.html')
def jilin_2(request):
    return render(request,'吉林各工资占比饼图.html')
def jilin_3(request):
    return render(request,'吉林公司规模象型柱图.html')
def jilin_4(request):
    return render(request,'吉林经验要求漏斗图.html')
def jilin_5(request):
    return render(request,'吉林热门行业词云图.html')

def liaoning_1(request):
    return render(request,'辽宁岗位数量分布地图.html')
def liaoning_2(request):
    return render(request,'辽宁各工资占比饼图.html')
def liaoning_3(request):
    return render(request,'辽宁公司规模象型柱图.html')
def liaoning_4(request):
    return render(request,'辽宁经验要求漏斗图.html')
def liaoning_5(request):
    return render(request,'辽宁热门行业词云图.html')

def neimenggu_1(request):
    return render(request,'内蒙古岗位数量分布地图.html')
def neimenggu_2(request):
    return render(request,'内蒙古各工资占比饼图.html')
def neimenggu_3(request):
    return render(request,'内蒙古公司规模象型柱图.html')
def neimenggu_4(request):
    return render(request,'内蒙古经验要求漏斗图.html')
def neimenggu_5(request):
    return render(request,'内蒙古热门行业词云图.html')

def ningxia_1(request):
    return render(request,'宁夏岗位数量分布地图.html')
def ningxia_2(request):
    return render(request,'宁夏各工资占比饼图.html')
def ningxia_3(request):
    return render(request,'宁夏公司规模象型柱图.html')
def ningxia_4(request):
    return render(request,'宁夏经验要求漏斗图.html')
def ningxia_5(request):
    return render(request,'宁夏热门行业词云图.html')

def qinghai_1(request):
    return render(request,'青海岗位数量分布地图.html')
def qinghai_2(request):
    return render(request,'青海各工资占比饼图.html')
def qinghai_3(request):
    return render(request,'青海公司规模象型柱图.html')
def qinghai_4(request):
    return render(request,'青海经验要求漏斗图.html')
def qinghai_5(request):
    return render(request,'青海热门行业词云图.html')

def shandong_1(request):
    return render(request,'山东岗位数量分布地图.html')
def shandong_2(request):
    return render(request,'山东各工资占比饼图.html')
def shandong_3(request):
    return render(request,'山东公司规模象型柱图.html')
def shandong_4(request):
    return render(request,'山东经验要求漏斗图.html')
def shandong_5(request):
    return render(request,'山东热门行业词云图.html')

def shanghai_1(request):
    return render(request,'上海岗位数量分布地图.html')
def shanghai_2(request):
    return render(request,'上海各工资占比饼图.html')
def shanghai_3(request):
    return render(request,'上海公司规模象型柱图.html')
def shanghai_4(request):
    return render(request,'上海经验要求漏斗图.html')
def shanghai_5(request):
    return render(request,'上海热门行业词云图.html')

def shanxi_1(request):
    return render(request,'陕西岗位数量分布地图.html')
def shanxi_2(request):
    return render(request,'陕西各工资占比饼图.html')
def shanxi_3(request):
    return render(request,'陕西公司规模象型柱图.html')
def shanxi_4(request):
    return render(request,'陕西经验要求漏斗图.html')
def shanxi_5(request):
    return render(request,'陕西热门行业词云图.html')

def shanxicu_1(request):
    return render(request,'山西岗位数量分布地图.html')
def shanxicu_2(request):
    return render(request,'山西各工资占比饼图.html')
def shanxicu_3(request):
    return render(request,'山西公司规模象型柱图.html')
def shanxicu_4(request):
    return render(request,'山西经验要求漏斗图.html')
def shanxicu_5(request):
    return render(request,'山西热门行业词云图.html')

def shenzhen_1(request):
    return render(request,'深圳岗位数量分布地图.html')
def shenzhen_2(request):
    return render(request,'深圳各工资占比饼图.html')
def shenzhen_3(request):
    return render(request,'深圳公司规模象型柱图.html')
def shenzhen_4(request):
    return render(request,'深圳经验要求漏斗图.html')
def shenzhen_5(request):
    return render(request,'深圳热门行业词云图.html')

def sichuan_1(request):
    return render(request,'四川岗位数量分布地图.html')
def sichuan_2(request):
    return render(request,'四川各工资占比饼图.html')
def sichuan_3(request):
    return render(request,'四川公司规模象型柱图.html')
def sichuan_4(request):
    return render(request,'四川经验要求漏斗图.html')
def sichuan_5(request):
    return render(request,'四川热门行业词云图.html')

def tianjin_1(request):
    return render(request,'天津岗位数量分布地图.html')
def tianjin_2(request):
    return render(request,'天津各工资占比饼图.html')
def tianjin_3(request):
    return render(request,'天津公司规模象型柱图.html')
def tianjin_4(request):
    return render(request,'天津经验要求漏斗图.html')
def tianjin_5(request):
    return render(request,'天津热门行业词云图.html')

def xinjiang_1(request):
    return render(request,'新疆岗位数量分布地图.html')
def xinjiang_2(request):
    return render(request,'新疆各工资占比饼图.html')
def xinjiang_3(request):
    return render(request,'新疆公司规模象型柱图.html')
def xinjiang_4(request):
    return render(request,'新疆经验要求漏斗图.html')
def xinjiang_5(request):
    return render(request,'新疆热门行业词云图.html')

def xizang_1(request):
    return render(request,'西藏岗位数量分布地图.html')
def xizang_2(request):
    return render(request,'西藏各工资占比饼图.html')
def xizang_3(request):
    return render(request,'西藏公司规模象型柱图.html')
def xizang_4(request):
    return render(request,'西藏经验要求漏斗图.html')
def xizang_5(request):
    return render(request,'西藏热门行业词云图.html')

def yunnan_1(request):
    return render(request,'云南岗位数量分布地图.html')
def yunnan_2(request):
    return render(request,'云南各工资占比饼图.html')
def yunnan_3(request):
    return render(request,'云南公司规模象型柱图.html')
def yunnan_4(request):
    return render(request,'云南经验要求漏斗图.html')
def yunnan_5(request):
    return render(request,'云南热门行业词云图.html')

def zhejiang_1(request):
    return render(request,'浙江岗位数量分布地图.html')
def zhejiang_2(request):
    return render(request,'浙江各工资占比饼图.html')
def zhejiang_3(request):
    return render(request,'浙江公司规模象型柱图.html')
def zhejiang_4(request):
    return render(request,'浙江经验要求漏斗图.html')
def zhejiang_5(request):
    return render(request,'浙江热门行业词云图.html')





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

