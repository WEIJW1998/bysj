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
sql = "SELECT category as xxx,count(*) as aaa FROM qcwy_all GROUP BY xxx order by aaa DESC;"
cursor.execute(sql)
hhh = cursor.fetchall()

print(hhh)
print(type(hhh))


data = []
for item in hhh:
    data.append(item)
print(data)


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
    .add(series_name="全国热门行业词云图", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="全国热门行业词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("全国热门行业词云图.html")
)
