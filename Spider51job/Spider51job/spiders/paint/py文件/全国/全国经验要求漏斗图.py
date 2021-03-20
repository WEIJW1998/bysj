from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType
import pymysql
from pyecharts.charts import Funnel

# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='123456', charset='utf8')
conn.select_db('qcwyDB')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "SELECT experience ,count(*) as aaa FROM qcwy_all GROUP BY experience order by aaa DESC LIMIT 8;"
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

wu_num = 0
wu_in = 0
zai_in = 0

for i in range(0, len(aaa)):
    if (aaa[i] == "无需经验"):
        wu_num = bbb[i]
        wu_in = i
    if (aaa[i] == "在校生/应届生"):
        zai_in = i


bbb[zai_in] += bbb[wu_in]
aaa.pop(wu_in)
bbb.pop(wu_in)

print(aaa)
print(bbb)

# 关闭数据库连接
conn.close()


c = (
    Funnel()
    .add(
        "",
        [list(z) for z in zip(aaa, bbb)],
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
    .render("全国经验要求漏斗图.html")
)
