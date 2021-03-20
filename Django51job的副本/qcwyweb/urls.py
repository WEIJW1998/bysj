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
    path('shanxicu', views.shanxicu, name="shanxicu"),
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


#---------------------------------------------------------------------------------

    path('全国各地区岗位数量分布地图', views.quanguo_1, name="全国各地区岗位数量分布地图"),
    path('全国各地区岗位数量条形图', views.quanguo_2, name="全国各地区岗位数量条形图"),
    path('全国各地区岗位数量折线图', views.quanguo_11, name="全国各地区岗位数量折线图"),
    path('全国各工资占比饼图', views.quanguo_3, name="全国各工资占比饼图"),
    path('全国各地区高等教育岗位数量分布地图', views.quanguo_4, name="全国各地区高等教育岗位数量分布地图"),
    path('全国各地区普通教育岗位数量分布地图', views.quanguo_5, name="全国各地区普通教育岗位数量分布地图"),

    path('全国公司规模象型柱图', views.quanguo_6, name="全国公司规模象型柱图"),
    path('全国经验要求漏斗图', views.quanguo_7, name="全国经验要求漏斗图"),
    path('全国城市词云图', views.quanguo_8, name="全国城市词云图"),
    path('全国公司待遇词云图', views.quanguo_9, name="全国公司待遇词云图"),
    path('全国热门行业词云图', views.quanguo_10, name="全国热门行业词云图"),
    # path('toregister/', views.toRegister),
    # path('register/', views.register),
#---------------------------------------------------------------------------------

    path('安徽岗位数量分布地图', views.anhui_1, name="安徽岗位数量分布地图"),
    path('安徽各工资占比饼图', views.anhui_2, name="安徽各工资占比饼图"),
    path('安徽公司规模象型柱图', views.anhui_3, name="安徽公司规模象型柱图"),
    path('安徽经验要求漏斗图', views.anhui_4, name="安徽经验要求漏斗图"),
    path('安徽热门行业词云图', views.anhui_5, name="安徽热门行业词云图"),

    path('北京岗位数量分布地图', views.beijing_1, name="北京岗位数量分布地图"),
    path('北京各工资占比饼图', views.beijing_2, name="北京各工资占比饼图"),
    path('北京公司规模象型柱图', views.beijing_3, name="北京公司规模象型柱图"),
    path('北京经验要求漏斗图', views.beijing_4, name="北京经验要求漏斗图"),
    path('北京热门行业词云图', views.beijing_5, name="北京热门行业词云图"),

    path('重庆岗位数量分布地图', views.chongqing_1, name="重庆岗位数量分布地图"),
    path('重庆各工资占比饼图', views.chongqing_2, name="重庆各工资占比饼图"),
    path('重庆公司规模象型柱图', views.chongqing_3, name="重庆公司规模象型柱图"),
    path('重庆经验要求漏斗图', views.chongqing_4, name="重庆经验要求漏斗图"),
    path('重庆热门行业词云图', views.chongqing_5, name="重庆热门行业词云图"),

    path('福建岗位数量分布地图', views.fujian_1, name="福建岗位数量分布地图"),
    path('福建各工资占比饼图', views.fujian_2, name="福建各工资占比饼图"),
    path('福建公司规模象型柱图', views.fujian_3, name="福建公司规模象型柱图"),
    path('福建经验要求漏斗图', views.fujian_4, name="福建经验要求漏斗图"),
    path('福建热门行业词云图', views.fujian_5, name="福建热门行业词云图"),

    path('甘肃岗位数量分布地图', views.gansu_1, name="甘肃岗位数量分布地图"),
    path('甘肃各工资占比饼图', views.gansu_2, name="甘肃各工资占比饼图"),
    path('甘肃公司规模象型柱图', views.gansu_3, name="甘肃公司规模象型柱图"),
    path('甘肃经验要求漏斗图', views.gansu_4, name="甘肃经验要求漏斗图"),
    path('甘肃热门行业词云图', views.gansu_5, name="甘肃热门行业词云图"),

    path('广东岗位数量分布地图', views.guangdong_1, name="广东岗位数量分布地图"),
    path('广东各工资占比饼图', views.guangdong_2, name="广东各工资占比饼图"),
    path('广东公司规模象型柱图', views.guangdong_3, name="广东公司规模象型柱图"),
    path('广东经验要求漏斗图', views.guangdong_4, name="广东经验要求漏斗图"),
    path('广东热门行业词云图', views.guangdong_5, name="广东热门行业词云图"),

    path('广西岗位数量分布地图', views.guangxi_1, name="广西岗位数量分布地图"),
    path('广西各工资占比饼图', views.guangxi_2, name="广西各工资占比饼图"),
    path('广西公司规模象型柱图', views.guangxi_3, name="广西公司规模象型柱图"),
    path('广西经验要求漏斗图', views.guangxi_4, name="广西经验要求漏斗图"),
    path('广西热门行业词云图', views.guangxi_5, name="广西热门行业词云图"),

    path('广州岗位数量分布地图', views.guangzhou_1, name="广州岗位数量分布地图"),
    path('广州各工资占比饼图', views.guangzhou_2, name="广州各工资占比饼图"),
    path('广州公司规模象型柱图', views.guangzhou_3, name="广州公司规模象型柱图"),
    path('广州经验要求漏斗图', views.guangzhou_4, name="广州经验要求漏斗图"),
    path('广州热门行业词云图', views.guangzhou_5, name="广州热门行业词云图"),

    path('贵州岗位数量分布地图', views.guizhou_1, name="贵州岗位数量分布地图"),
    path('贵州各工资占比饼图', views.guizhou_2, name="贵州各工资占比饼图"),
    path('贵州公司规模象型柱图', views.guizhou_3, name="贵州公司规模象型柱图"),
    path('贵州经验要求漏斗图', views.guizhou_4, name="贵州经验要求漏斗图"),
    path('贵州热门行业词云图', views.guizhou_5, name="贵州热门行业词云图"),

    path('海南岗位数量分布地图', views.hainan_1, name="海南岗位数量分布地图"),
    path('海南各工资占比饼图', views.hainan_2, name="海南各工资占比饼图"),
    path('海南公司规模象型柱图', views.hainan_3, name="海南公司规模象型柱图"),
    path('海南经验要求漏斗图', views.hainan_4, name="海南经验要求漏斗图"),
    path('海南热门行业词云图', views.hainan_5, name="海南热门行业词云图"),

    path('河北岗位数量分布地图', views.hebei_1, name="河北岗位数量分布地图"),
    path('河北各工资占比饼图', views.hebei_2, name="河北各工资占比饼图"),
    path('河北公司规模象型柱图', views.hebei_3, name="河北公司规模象型柱图"),
    path('河北经验要求漏斗图', views.hebei_4, name="河北经验要求漏斗图"),
    path('河北热门行业词云图', views.hebei_5, name="河北热门行业词云图"),

    path('黑龙江岗位数量分布地图', views.heilongjiang_1, name="黑龙江岗位数量分布地图"),
    path('黑龙江各工资占比饼图', views.heilongjiang_2, name="黑龙江各工资占比饼图"),
    path('黑龙江公司规模象型柱图', views.heilongjiang_3, name="黑龙江公司规模象型柱图"),
    path('黑龙江经验要求漏斗图', views.heilongjiang_4, name="黑龙江经验要求漏斗图"),
    path('黑龙江热门行业词云图', views.heilongjiang_5, name="黑龙江热门行业词云图"),

    path('河南岗位数量分布地图', views.henan_1, name="河南岗位数量分布地图"),
    path('河南各工资占比饼图', views.henan_2, name="河南各工资占比饼图"),
    path('河南公司规模象型柱图', views.henan_3, name="河南公司规模象型柱图"),
    path('河南经验要求漏斗图', views.henan_4, name="河南经验要求漏斗图"),
    path('河南热门行业词云图', views.henan_5, name="河南热门行业词云图"),

    path('湖北岗位数量分布地图', views.hubei_1, name="湖北岗位数量分布地图"),
    path('湖北各工资占比饼图', views.hubei_2, name="湖北各工资占比饼图"),
    path('湖北公司规模象型柱图', views.hubei_3, name="湖北公司规模象型柱图"),
    path('湖北经验要求漏斗图', views.hubei_4, name="湖北经验要求漏斗图"),
    path('湖北热门行业词云图', views.hubei_5, name="湖北热门行业词云图"),

    path('湖南岗位数量分布地图', views.hunan_1, name="湖南岗位数量分布地图"),
    path('湖南各工资占比饼图', views.hunan_2, name="湖南各工资占比饼图"),
    path('湖南公司规模象型柱图', views.hunan_3, name="湖南公司规模象型柱图"),
    path('湖南经验要求漏斗图', views.hunan_4, name="湖南经验要求漏斗图"),
    path('湖南热门行业词云图', views.hunan_5, name="湖南热门行业词云图"),

    path('江苏岗位数量分布地图', views.jiangsu_1, name="江苏岗位数量分布地图"),
    path('江苏各工资占比饼图', views.jiangsu_2, name="江苏各工资占比饼图"),
    path('江苏公司规模象型柱图', views.jiangsu_3, name="江苏公司规模象型柱图"),
    path('江苏经验要求漏斗图', views.jiangsu_4, name="江苏经验要求漏斗图"),
    path('江苏热门行业词云图', views.jiangsu_5, name="江苏热门行业词云图"),

    path('江西岗位数量分布地图', views.jiangxi_1, name="江西岗位数量分布地图"),
    path('江西各工资占比饼图', views.jiangxi_2, name="江西各工资占比饼图"),
    path('江西公司规模象型柱图', views.jiangxi_3, name="江西公司规模象型柱图"),
    path('江西经验要求漏斗图', views.jiangxi_4, name="江西经验要求漏斗图"),
    path('江西热门行业词云图', views.jiangxi_5, name="江西热门行业词云图"),

    path('吉林岗位数量分布地图', views.jilin_1, name="吉林岗位数量分布地图"),
    path('吉林各工资占比饼图', views.jilin_2, name="吉林各工资占比饼图"),
    path('吉林公司规模象型柱图', views.jilin_3, name="吉林公司规模象型柱图"),
    path('吉林经验要求漏斗图', views.jilin_4, name="吉林经验要求漏斗图"),
    path('吉林热门行业词云图', views.jilin_5, name="吉林热门行业词云图"),

    path('辽宁岗位数量分布地图', views.liaoning_1, name="辽宁岗位数量分布地图"),
    path('辽宁各工资占比饼图', views.liaoning_2, name="辽宁各工资占比饼图"),
    path('辽宁公司规模象型柱图', views.liaoning_3, name="辽宁公司规模象型柱图"),
    path('辽宁经验要求漏斗图', views.liaoning_4, name="辽宁经验要求漏斗图"),
    path('辽宁热门行业词云图', views.liaoning_5, name="辽宁热门行业词云图"),

    path('内蒙古岗位数量分布地图', views.neimenggu_1, name="内蒙古岗位数量分布地图"),
    path('内蒙古各工资占比饼图', views.neimenggu_2, name="内蒙古各工资占比饼图"),
    path('内蒙古公司规模象型柱图', views.neimenggu_3, name="内蒙古公司规模象型柱图"),
    path('内蒙古经验要求漏斗图', views.neimenggu_4, name="内蒙古经验要求漏斗图"),
    path('内蒙古热门行业词云图', views.neimenggu_5, name="内蒙古热门行业词云图"),

    path('宁夏岗位数量分布地图', views.ningxia_1, name="宁夏岗位数量分布地图"),
    path('宁夏各工资占比饼图', views.ningxia_2, name="宁夏各工资占比饼图"),
    path('宁夏公司规模象型柱图', views.ningxia_3, name="宁夏公司规模象型柱图"),
    path('宁夏经验要求漏斗图', views.ningxia_4, name="宁夏经验要求漏斗图"),
    path('宁夏热门行业词云图', views.ningxia_5, name="宁夏热门行业词云图"),

    path('青海岗位数量分布地图', views.qinghai_1, name="青海岗位数量分布地图"),
    path('青海各工资占比饼图', views.qinghai_2, name="青海各工资占比饼图"),
    path('青海公司规模象型柱图', views.qinghai_3, name="青海公司规模象型柱图"),
    path('青海经验要求漏斗图', views.qinghai_4, name="青海经验要求漏斗图"),
    path('青海热门行业词云图', views.qinghai_5, name="青海热门行业词云图"),

    path('山东岗位数量分布地图', views.shandong_1, name="山东岗位数量分布地图"),
    path('山东各工资占比饼图', views.shandong_2, name="山东各工资占比饼图"),
    path('山东公司规模象型柱图', views.shandong_3, name="山东公司规模象型柱图"),
    path('山东经验要求漏斗图', views.shandong_4, name="山东经验要求漏斗图"),
    path('山东热门行业词云图', views.shandong_5, name="山东热门行业词云图"),

    path('上海岗位数量分布地图', views.shanghai_1, name="上海岗位数量分布地图"),
    path('上海各工资占比饼图', views.shanghai_2, name="上海各工资占比饼图"),
    path('上海公司规模象型柱图', views.shanghai_3, name="上海公司规模象型柱图"),
    path('上海经验要求漏斗图', views.shanghai_4, name="上海经验要求漏斗图"),
    path('上海热门行业词云图', views.shanghai_5, name="上海热门行业词云图"),

    path('陕西岗位数量分布地图', views.shanxi_1, name="陕西岗位数量分布地图"),
    path('陕西各工资占比饼图', views.shanxi_2, name="陕西各工资占比饼图"),
    path('陕西公司规模象型柱图', views.shanxi_3, name="陕西公司规模象型柱图"),
    path('陕西经验要求漏斗图', views.shanxi_4, name="陕西经验要求漏斗图"),
    path('陕西热门行业词云图', views.shanxi_5, name="陕西热门行业词云图"),

    path('山西岗位数量分布地图', views.shanxicu_1, name="山西岗位数量分布地图"),
    path('山西各工资占比饼图', views.shanxicu_2, name="山西各工资占比饼图"),
    path('山西公司规模象型柱图', views.shanxicu_3, name="山西公司规模象型柱图"),
    path('山西经验要求漏斗图', views.shanxicu_4, name="山西经验要求漏斗图"),
    path('山西热门行业词云图', views.shanxicu_5, name="山西热门行业词云图"),

    path('深圳岗位数量分布地图', views.shenzhen_1, name="深圳岗位数量分布地图"),
    path('深圳各工资占比饼图', views.shenzhen_2, name="深圳各工资占比饼图"),
    path('深圳公司规模象型柱图', views.shenzhen_3, name="深圳公司规模象型柱图"),
    path('深圳经验要求漏斗图', views.shenzhen_4, name="深圳经验要求漏斗图"),
    path('深圳热门行业词云图', views.shenzhen_5, name="深圳热门行业词云图"),

    path('四川岗位数量分布地图', views.sichuan_1, name="四川岗位数量分布地图"),
    path('四川各工资占比饼图', views.sichuan_2, name="四川各工资占比饼图"),
    path('四川公司规模象型柱图', views.sichuan_3, name="四川公司规模象型柱图"),
    path('四川经验要求漏斗图', views.sichuan_4, name="四川经验要求漏斗图"),
    path('四川热门行业词云图', views.sichuan_5, name="四川热门行业词云图"),

    path('天津岗位数量分布地图', views.tianjin_1, name="天津岗位数量分布地图"),
    path('天津各工资占比饼图', views.tianjin_2, name="天津各工资占比饼图"),
    path('天津公司规模象型柱图', views.tianjin_3, name="天津公司规模象型柱图"),
    path('天津经验要求漏斗图', views.tianjin_4, name="天津经验要求漏斗图"),
    path('天津热门行业词云图', views.tianjin_5, name="天津热门行业词云图"),

    path('新疆岗位数量分布地图', views.xinjiang_1, name="新疆岗位数量分布地图"),
    path('新疆各工资占比饼图', views.xinjiang_2, name="新疆各工资占比饼图"),
    path('新疆公司规模象型柱图', views.xinjiang_3, name="新疆公司规模象型柱图"),
    path('新疆经验要求漏斗图', views.xinjiang_4, name="新疆经验要求漏斗图"),
    path('新疆热门行业词云图', views.xinjiang_5, name="新疆热门行业词云图"),

    path('西藏岗位数量分布地图', views.xizang_1, name="西藏岗位数量分布地图"),
    path('西藏各工资占比饼图', views.xizang_2, name="西藏各工资占比饼图"),
    path('西藏公司规模象型柱图', views.xizang_3, name="西藏公司规模象型柱图"),
    path('西藏经验要求漏斗图', views.xizang_4, name="西藏经验要求漏斗图"),
    path('西藏热门行业词云图', views.xizang_5, name="西藏热门行业词云图"),

    path('云南岗位数量分布地图', views.yunnan_1, name="云南岗位数量分布地图"),
    path('云南各工资占比饼图', views.yunnan_2, name="云南各工资占比饼图"),
    path('云南公司规模象型柱图', views.yunnan_3, name="云南公司规模象型柱图"),
    path('云南经验要求漏斗图', views.yunnan_4, name="云南经验要求漏斗图"),
    path('云南热门行业词云图', views.yunnan_5, name="云南热门行业词云图"),

    path('浙江岗位数量分布地图', views.zhejiang_1, name="浙江岗位数量分布地图"),
    path('浙江各工资占比饼图', views.zhejiang_2, name="浙江各工资占比饼图"),
    path('浙江公司规模象型柱图', views.zhejiang_3, name="浙江公司规模象型柱图"),
    path('浙江经验要求漏斗图', views.zhejiang_4, name="浙江经验要求漏斗图"),
    path('浙江热门行业词云图', views.zhejiang_5, name="浙江热门行业词云图"),


    #---------------------------------------------------------------------------------













]