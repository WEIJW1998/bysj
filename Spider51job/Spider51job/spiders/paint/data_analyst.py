from pyecharts import options as opts
from pyecharts.charts import Bar
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='123456', charset='utf8')
conn.select_db('qcwyDB')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "select substring_index(city,'-',1) as xxx,count(*) from qcwy_table_copy1 GROUP BY xxx order by count(*) DESC limit 50;"
cursor.execute(sql)
hhh = cursor.fetchall()

xxx = list(hhh)
for i in range(len(xxx)):
    xxx[i] = list(xxx[i])


# 统一城市
# str1 = "-"


aaa = []
bbb = []

for item in xxx:
    aaa.append(item[0])
    bbb.append(item[1])

# xx = -1

# for i in aaa:
#     xx += 1
#     if(i.find("-")+1):
#         i = (i[:i.index(str1)])
#         aaa[xx] = i
#     else:
#         continue

print(aaa)
print(bbb)

# 关闭数据库连接
conn.close()

c = (
    Bar()
    .add_xaxis(aaa)
    .add_yaxis("地区", bbb)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-60)),
        title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
    )
    .render("bar_city.html")
)
