import scrapy
from scrapy.http import Request
from fashionWebScraping.items import FashionwebscrapingItem
from fashionWebScraping.items import ImgData
from urllib.parse import urlparse

import csv


class FashionhepsiburadaSpider(scrapy.Spider):
    name = "fashionHEPSIBURADA"

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    allowed_domains = ["hepsiburada.com"]
    start_urls = ["https://hepsiburada.com"]

    def start_requests(self):
        # Read main category links from a csv file
        with open("./csvFiles/SpiderMainCategoryLinksHEPSIBURADA.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row['url']
                # Change the offset value incrementally to navigate through the product list
                # You can play with the range value according to maximum product quantity
                link_urls = [url.format(i) for i in range(1, 10)]

                for link_url in link_urls:
                    print(link_url)
                    # Pass each link containing 100 products to the parse_product_pages function with the gender metadata
                    request = Request(link_url, callback=self.parse_product_pages, meta={
                                      'gender': row['gender']})
                    yield request

    def parse_product_pages(self, response):
        item = FashionwebscrapingItem()
        content = response.xpath('//ul')

        for product_content in content.xpath('//li[@class="productListContent-zAP0Y5msy8OHn5z7T_K_"]'):

            image_urls = []

            # get the product details and populate the items
            url = "https://www.hepsiburada.com" + \
                product_content.xpath('.//a/@href').extract_first()

            parsed_url = urlparse(url)
            path = parsed_url.path
            if '-p-' in path:
                separator = '-p-'
            elif '-pm-' in path:
                separator = '-pm-'
            else:
                print("Product ID separator not found in the URL")

            item['productId'] = path.split(separator)[-1]
            item['productName'] = product_content.xpath(
                './/h3/text()').extract_first()

            item['priceOriginal'] = product_content.xpath(
                './/div[@data-test-id="price-prev-price"]/div/text()').extract_first()

            if item['priceOriginal'] == None:
                item['priceOriginal'] = product_content.xpath(
                    './/div[@data-test-id="price-current-price"]/text()').extract_first()

            item['priceSale'] = product_content.xpath(
                './/div[@data-test-id="price-current-price"]/text()').extract_first()

            # item['priceSale']=product_content.xpath('.//div[@class="price-value"]').extract_first()

            # if item['priceSale']==None:
            #    item['priceSale']=product_content.xpath('.//div[@class="moria-ProductCard-kUDchF clTZl sy6qqmcj2na"]/text()').extract_first()

            # ['priceSale'] = ''.join((ch if ch in '0123456789,.' else '') for ch in item['priceSale'])

            item['imageLink'] = product_content.xpath(
                './/img/@src').extract_first()
            item['productLink'] = "https://www.hepsiburada.com" + \
                product_content.xpath('.//a/@href').extract_first()

            image_urls.append(item['imageLink'])

            item['company'] = "HEPSIBURADA"
            item['gender'] = response.meta['gender']

            if item['productId']==None:
              break

            yield (item)
            yield ImgData(image_urls=image_urls)
