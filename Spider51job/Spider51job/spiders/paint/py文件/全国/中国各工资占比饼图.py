from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='123456', charset='utf8')
conn.select_db('qcwyDB')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "SELECT substring_index(city, '-', 1),salary from qcwy_all where salary not like '%元%';"
cursor.execute(sql)
hhh = cursor.fetchall()

xxx = list(hhh)

for i in range(len(xxx)):
    xxx[i] = list(xxx[i])

aaa = []
bbb = []


stra = []
strz = []

numsplit = []
strsplit = []

numa = []
numz = []

dw = []
sj = []

newsalary = []

for item in xxx:
    aaa.append(item[0])
    bbb.append(item[1])

mm = 0
for x in bbb:
    stra.append(x[:-3])
    strz.append(x[-3:])
    numsplit.append(stra[mm].split('-'))
    strsplit.append(strz[mm].split('/'))

    numa.append(float(numsplit[mm][0]))
    numz.append(float(numsplit[mm][1]))

    dw.append(strsplit[mm][0])
    sj.append(strsplit[mm][1])
    mm += 1

# print(aaa)
# print(bbb)


for i in range(0, len(numa)):
    if dw[i] == '万':
        numa[i] = numa[i]*10000
        numz[i] = numz[i]*10000
        newsalary.append(round((numa[i] + numz[i])/2))
    else:
        numa[i] = (numa[i])*1000
        numz[i] = (numz[i])*1000
        newsalary.append(round((numa[i] + numz[i]) / 2))

    if sj[i] == '年':
        newsalary[i] = round(newsalary[i]/12)
# print(newsalary)

salary1 = 0
salary2 = 0
salary3 = 0
salary4 = 0
salary5 = 0
salary6 = 0

for i in newsalary:
    if i < 5000:
        salary1 += 1
    elif 5000 <= i and i < 10000:
        salary2 += 1
    elif 10000 <= i and i < 15000:
        salary3 += 1
    elif 15000 <= i and i < 20000:
        salary4 += 1
    elif 20000 <= i and i < 30000:
        salary5 += 1
    elif 30000 <= i:
        salary6 += 1

strarr = ('5k以下', '5k-1w', '1w-1.5w', '1.5w-2w', '2w-3w', '3w以上')
numarr = (salary1, salary2, salary3, salary4, salary5, salary6)

# 关闭数据库连接
conn.close()


c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(strarr, numarr)],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各工资占比饼图"),
        legend_opts=opts.LegendOpts(pos_left="15%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("中国各工资占比饼图.html")
)
