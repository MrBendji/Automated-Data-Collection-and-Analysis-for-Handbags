import scrapy
from scrapy import Request
import csv
from fashionWebScraping.items import FashionwebscrapingItem
from fashionWebScraping.items import ImgData


class FashionkotonSpider(scrapy.Spider):
    name = 'fashionKOTON'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    allowed_domains = ['www.koton.com']
    start_urls = ['http://www.koton.com/']

    def start_requests(self):
        with open("./csvFiles/SpiderMainCategoryLinksKOTON.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row['url'].split()
                print(url)
                request = Request(row['url'], callback=self.parse_product_pages, meta={
                                  'gender': row['gender']})
                yield request

    def parse_product_pages(self, response):
        max_page_numbers = response.xpath(
            '//div[@class="hidden js-page-count"]/text()').extract()
        print(max_page_numbers)
        print(response.meta['gender'])
        pageList = []
        for max_page_number in max_page_numbers:
            print(max_page_number)
            try:
                pageList.append(int(max_page_number))
            except ValueError:
                print("hata")
                pass
        print(pageList)
        if pageList:
            max_page_number_one = max(pageList)
        else:
            max_page_number_one = 0
        print(max_page_number_one)
        link_urls = [response.request.url+'?q=%3Arelevance&psize=192&page={}'.format(
            i) for i in range(0, max_page_number_one)]
        for link_url in link_urls:
            print(link_url)
            yield response.follow(link_url, callback=self.parse, meta={'gender': response.meta['gender']})

    def parse(self, response):
        item = FashionwebscrapingItem()
        fullContent = response.xpath(
            '//div[@class="list__products"]')
        for content in fullContent.xpath(
                '//div[@class="js-product-wrapper product-item"]'):
            image_urls = []
            item['company'] = "KOTON"
            item['gender'] = response.meta['gender']
            item['productName'] = content.xpath(
                './/a[@class="js-product-link product-link"]/text()').extract_first()
            item['imageLink'] = content.xpath(
                './/img/@src').extract_first()
            item['productLink'] = "https://www.koton.com" + \
                content.xpath('.//a/@href').extract_first()
            image_urls.append(item['imageLink'])
            item['priceOriginal'] = content.xpath(
                '@data-price').extract_first()
            item['priceSale'] = item['priceOriginal']
            # if item['priceOriginal'] == None:
            #     item['priceOriginal'] = content.xpath(
            #         './/span[@class="insteadPrice"]/s/text()').extract_first()
            #     item['priceSale'] = content.xpath(
            #         './/span[@class="newPrice"]/text()').extract_first()
            item['productId'] = content.xpath(
                '@data-sku').extract_first()

            yield item
            yield ImgData(image_urls=image_urls)
