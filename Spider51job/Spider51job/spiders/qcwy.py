import scrapy
from Spider51job.items import Spider51JobItem


class QcwySpider(scrapy.Spider):
    name = 'qcwy'
    allowed_domains = ['51job.com']

    baseURL = "https://search.51job.com/list/000000,000000,0000,00,9,99,+,2,"
    offset = 1
    start_urls = [baseURL+str(offset)+".html"]

    # start_urls = [
    #     'https://search.51job.com/list/000000,000000,0000,00,9,99,+,2,1.html']

    def parse(self, response):

        # selectors = response.xpath('//div[@class="j_joblist"]/div[@class="e"]/a[@class="el"]/p/span[@class="jname at"]/text()'

        try:

            # 用来存储所有的item字段
            # items = []
            # 创建item字段对象，用来存储信息
            item = Spider51JobItem()

            # 职位
            job_name = response.xpath('.').re('"job_name":"(.*?)",')
            # 去掉职位的 \ 符号
            job_name = [i.replace('\\', '') for i in job_name]

            # 公司名称
            company_name = response.xpath('.').re('"company_name":"(.*?)",')

            # 公司规模
            companysize = response.xpath('.').re('"companysize_text":"(.*?)",')

            # 城市
            city = response.xpath('.').re('"workarea_text":"(.*?)",')

            # 薪酬
            salary = response.xpath('.').re('"providesalary_text":"(.*?)",')
            # 去掉薪酬的 \ 符号
            salary = [i.replace('\\', '') for i in salary]

            # 公司所属行业
            category = response.xpath('.').re('"companyind_text":"(.*?)",')
            # 去掉公司所属行业 \ 符号
            category = [i.replace('\\', '') for i in category]

            # 属性
            attribute_text = response.xpath('.').re(
                '"attribute_text":(.*?),"companysize_text"')
            attribute_text = ['|'.join(eval(i)) for i in attribute_text]
            attribute_text = [i.replace('\\', '') for i in attribute_text]

            # 职位福利
            job_welfare = response.xpath('.').re('"jobwelf":"(.*?)",')

            # item_job_name = []
            # item_company_name = []
            # item_companysize = []
            # item_city = []
            # item_salary = []
            # item_category = []
            # item_attribute_text = []
            # item_job_welfare = []

            # item_job_name = job_name
            # item_company_name = company_name
            # item_companysize = companysize
            # item_city = city
            # item_salary = salary
            # item_category = category
            # item_attribute_text = attribute_text
            # item_job_welfare = job_welfare

            MaxPage = 2000
            if self.offset < MaxPage:
                self.offset += 1
                url = self.baseURL + str(self.offset) + ".html"
                yield scrapy.Request(url, callback=self.parse)

            # items.append(item)
            # return items

            # hhh = response.text
            # writefile('weijw.txt', str(companysize))

            # item['job_name'] = job_name[0]
            # item['company_name'] = company_name[0]
            # item['companysize'] = companysize[0]
            # item['city'] = city[0]
            # item['salary'] = salary[0]
            # item['category'] = category[0]
            # item['attribute_text'] = attribute_text[0]
            # item['job_welfare'] = job_welfare[0]

            # item['job_name'] = job_name[49]
            # item['company_name'] = company_name[49]
            # item['companysize'] = companysize[49]
            # item['city'] = city[49]
            # item['salary'] = salary[49]
            # item['category'] = category[49]
            # item['attribute_text'] = attribute_text[49]
            # item['job_welfare'] = job_welfare[49]

            for i in range(len(job_name)):

                item['job_name'] = job_name[i]
                item['company_name'] = company_name[i]
                item['companysize'] = companysize[i]
                item['city'] = city[i]
                item['salary'] = salary[i]
                item['category'] = category[i]
                item['attribute_text'] = attribute_text[i]
                item['job_welfare'] = job_welfare[i]
                yield item

            # print(job_name[0])
            # print(company_name[0])
            # print(companysize[0])
            # print(city[0])
            # print(salary[0])
            # print(category[0])
            # print(attribute_text[0])
            # print(job_welfare[0])

            # print(response.text)
            # yield item

        except Exception as e:
            print(e)


def writefile(file_name, content_str):
    with open(file_name, "w", encoding='utf-8', ) as f:
        f.write(content_str)
        f.close
