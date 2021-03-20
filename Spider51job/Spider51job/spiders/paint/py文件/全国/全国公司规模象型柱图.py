from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType
import pymysql


# 打开数据库连接
conn = pymysql.connect(host='localhost', user='root',
                       passwd='123456', charset='utf8')
conn.select_db('qcwyDB')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = "SELECT companysize ,count(*) as aaa FROM qcwy_all GROUP BY companysize order by aaa DESC LIMIT 7;"
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


c = (
    PictorialBar()
    .add_xaxis(aaa)
    .add_yaxis(
        "",
        bbb,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国公司规模象型柱图"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("全国公司规模象型柱图.html")
)
