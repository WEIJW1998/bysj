import scrapy
from Spider51job.items import Spider51JobItem


class QcwySpider(scrapy.Spider):
    name = 'qcwy'
    allowed_domains = ['51job.com']

    xxx = ["https://search.51job.com/list/092200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/201000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/281500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/010000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/092000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/141100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/231000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/241000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/280400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/280900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/060000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/141400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/161000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/231400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/280300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/072100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/172000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/221400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/250500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/252000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/271100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/280800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/030600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/131100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/231500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/030200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/092100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/141000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/271500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/290600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/030300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/081600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/141200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/141500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/161200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/191100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/221000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/221200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/280200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/281100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/031500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/072500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/211000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/250200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/081000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/092300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/102100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/111000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/141300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/191200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/211200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/231100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/250600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/271200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/271400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/231300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/271000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/031900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/081200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/221300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/250300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/261000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/271300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/020000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/030400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/031400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/040000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/072000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/131200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/191000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/201100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/221100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/290500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/300500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/050000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/072300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/231200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/280700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/080400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/100700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/101000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/140700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/150300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/281000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/281200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/290300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/311000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/151400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/161100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/180900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/181400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/191500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/211100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/281300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/281400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/032900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/070800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/081400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/102000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/130700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/131000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/161300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/191300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/200800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/201200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/210800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/220300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/230500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/240800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/241100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/250400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/290200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/310500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/320900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/030500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/030700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/031700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/031800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071000,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/071400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/081100,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/090800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/091400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/110500,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/120700,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/121600,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/160900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170200,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/170800,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/171400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/190300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/191400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/251300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/260300,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/270900,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/290400,000000,0000,00,9,99,+,2,",

           "https://search.51job.com/list/290400,000000,0000,00,9,99,+,2,"]

    link = 0

    baseURL = xxx[link]
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
            company_name = response.xpath(
                '.').re('"company_name":"(.*?)",')

            # 公司规模
            companysize = response.xpath('.').re(
                '"companysize_text":"(.*?)",')

            # 城市
            city = response.xpath('.').re('"workarea_text":"(.*?)",')

            # 薪酬
            salary = response.xpath('.').re(
                '"providesalary_text":"(.*?)",')
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

            # 总页码数
            total_page = response.xpath('.').re('"total_page":"(.*?)",')

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

            MaxPage = int(total_page[0])
            if self.offset < MaxPage:
                self.offset += 1
                url = self.baseURL + str(self.offset) + ".html"
                yield scrapy.Request(url, callback=self.parse)
            elif self.link < len(self.xxx):
                self.offset = 1
                self.link += 1
                self.baseURL = self.xxx[self.link]
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
