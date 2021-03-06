from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import pymysql
from pyecharts.charts import WordCloud

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='123456', charset='utf8')
conn.select_db('qcwyDB')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "select  job_welfare from qcwy_all where attribute_text like '%本科%' or attribute_text like '%硕士%' or attribute_text like '%应届生%' or attribute_text like '%博士%' or attribute_text like '%在校生/应届生%' ;"
cursor.execute(sql)
hhh = cursor.fetchall()

# print(hhh)
# print(type(hhh))


data = []
for item in hhh:
    data.extend(item)
# print(data)

strall = ""

for i in data:
    strall = strall + " " + i

# print(strall)


strarr = strall.split()
# print(strarr)


stat = {}

for strarr in strarr:
    if strarr not in stat:
        stat[strarr] = 1
    else:
        stat[strarr] += 1
# print(stat)


w = []
for item in stat.items():
    w.append(item)
for i in range(1, len(w)):
    for j in range(0, len(w)-1):
        if w[j][1] < w[j+1][1]:
            w[j], w[j+1] = w[j+1], w[j]
# print(w)


# xxx = list(hhh)
# for i in range(len(xxx)):
#     xxx[i] = list(xxx[i])

# print(xxx)

# aaa = []
# bbb = []

# for item in xxx:
#     aaa.append(item[0])
#     bbb.append(item[1])


# print(aaa)
# print(bbb)

# 关闭数据库连接
conn.close()


(
    WordCloud()
    .add(series_name="公司待遇词云图", data_pair=w, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="公司待遇词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("公司待遇词云图.html")
)
