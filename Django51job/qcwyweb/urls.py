from django.urls import path
from qcwyweb import views



urlpatterns = [
    path('', views.toLogin),
    path('index/', views.Login),
    path('index/quanguo/', views.toquanguo),
    path('index/diqu/', views.todiqu),
    path('beijing', views.beijing , name="beijing"),
    path('shanghai', views.shanghai , name="shanghai"),
    path('guangzhou', views.guangzhou , name="guangzhou"),
    path('shenzhen', views.shenzhen , name="shenzhen"),
    path('tianjin', views.tianjin , name="tianjin"),
    path('chongqing', views.chongqing , name="chongqing"),
    path('neimenggu', views.neimenggu , name="neimenggu"),
    path('guangxi', views.guangxi , name="guangxi"),
    path('xizang', views.xizang , name="xizang"),
    path('ningxia', views.ningxia , name="ningxia"),

    path('hebei', views.hebei , name="hebei"),
    path('xinjiang', views.xinjiang , name="xinjiang"),
    path('shanxi', views.shanxi , name="shanxi"),
    path('liaoning', views.liaoning , name="liaoning"),
    path('jilin', views.jilin , name="jilin"),
    path('heilongjiang', views.heilongjiang , name="heilongjiang"),
    path('jiangsu', views.jiangsu , name="jiangsu"),
    path('zhejiang', views.zhejiang , name="zhejiang"),
    path('anhui', views.anhui , name="anhui"),
    path('fujian', views.fujian , name="fujian"),

    path('jiangxi', views.jiangxi , name="jiangxi"),
    path('shandong', views.shandong , name="shandong"),
    path('henan', views.henan , name="henan"),
    path('hubei', views.hubei , name="hubei"),
    path('hunan', views.hunan , name="hunan"),
    path('guangdong', views.guangdong , name="guangdong"),
    path('hainan', views.hainan , name="hainan"),
    path('sichuan', views.sichuan , name="sichuan"),
    path('guizhou', views.guizhou , name="guizhou"),
    path('yunnan', views.yunnan , name="yunnan"),

    path('shanxi', views.shanxi , name="shanxi"),
    path('gansu', views.gansu , name="gansu"),
    path('qinghai', views.qinghai , name="qinghai"),




    path('中国各地区岗位数量分布地图', views.quanguo_1, name="中国各地区岗位数量分布地图"),
    path('中国各地区岗位数量条形图', views.quanguo_2, name="中国各地区岗位数量条形图"),
    path('中国各工资占比饼图', views.quanguo_3, name="中国各工资占比饼图"),
    path('中国各地区高等教育岗位数量分布地图', views.quanguo_4, name="中国各地区高等教育岗位数量分布地图"),
    path('中国各地区普通教育岗位数量分布地图', views.quanguo_5, name="中国各地区普通教育岗位数量分布地图"),
    # path('toregister/', views.toRegister),
    # path('register/', views.register),
]