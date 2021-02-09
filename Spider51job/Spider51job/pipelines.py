# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql


class Spider51JobPipeline:

    def __init__(self):
        # self.f = open("qcwy_piplines.json", "w", encoding='utf-8',)

        # 连接数据库
        self.conn = pymysql.connect(
            host='localhost', user='root', passwd='123456', charset='utf8')
        self.conn.select_db('qcwyDB')
        self.cur = self.conn.cursor()
        print("数据库连接成功！")

    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # self.f.write(str(content))

        # job_name = item.get("job_name", "N/A")
        # company_name = item.get("company_name", "N/A")
        # companysize = item.get("companysize", "N/A")
        # city = item.get("city", "N/A")
        # salary = item.get("salary", "N/A")
        # category = item.get("category", "N/A")
        # attribute_text = item.get("attribute_text", "N/A")
        # job_welfare = item.get("job_welfare", "N/A")

        job_name = item["job_name"]
        company_name = item["company_name"]
        companysize = item["companysize"]
        city = item["city"]
        salary = item["salary"]
        category = item["category"]
        attribute_text = item["attribute_text"]
        job_welfare = item["job_welfare"]

        params = (job_name,
                  company_name,
                  companysize,
                  city,
                  salary,
                  category,
                  attribute_text,
                  job_welfare
                  )

        # Sql语句
        sql = "insert into qcwytable(" \
            "job_name,"\
            "company_name," \
            "companysize," \
            "city," \
            "salary," \
            "category," \
            "attribute_text," \
            "job_welfare"\
            ") values(%s,%s,%s,%s,%s,%s,%s,%s);"

        print('+----------------------------------------------------------------------------------')
        print('|'+item['job_name'])
        print('|'+item['company_name'])
        print('|'+item['companysize'])
        print('|'+item['city'])
        print('|'+item['salary'])
        print('|'+item['category'])
        print('|'+item['attribute_text'])
        print('|'+item['job_welfare'])
        print('+----------------------------------------------------------------------------------\n')

        try:

            self.cur.execute(sql, params)
            self.conn.commit()

        except Exception as error:
            print('错误：')
            print(error)
        print('---------------sql执行成功---------------')
        # return item

    def close_spider(self, spider):

        # 关闭游标和连接
        self.cur.close()
        self.conn.close()

    # return item
