from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.charts import Line

import pymysql

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='123456', charset='utf8')
conn.select_db('qcwyDB')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "SELECT substring_index(city,'-',1) as xxx,sum(num) as aaa FROM qcwy_all GROUP BY xxx order by aaa DESC;"
cursor.execute(sql)
hhh = cursor.fetchall()

xxx = list(hhh)
for i in range(len(xxx)):
    xxx[i] = list(xxx[i])

aaa = []
bbb = []

for item in xxx:
    aaa.append(item[0])
    bbb.append(item[1])


print(aaa)
print(bbb)

# 关闭数据库连接
conn.close()


(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=aaa)
    .add_yaxis(
        series_name="",
        y_axis=bbb,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("中国各地区岗位数量折线图.html")
)
