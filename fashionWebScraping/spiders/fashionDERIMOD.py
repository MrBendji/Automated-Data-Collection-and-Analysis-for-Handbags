import scrapy
from scrapy.http import Request
from fashionWebScraping.items import FashionwebscrapingItem
from fashionWebScraping.items import ImgData

import csv


class FashionderimodSpider(scrapy.Spider):
    name = "fashionDERIMOD"
    allowed_domains = ["derimod.com"]
    start_urls = ["https://derimod.com"]

    def start_requests(self):
        # Read main category links from a csv file
        with open("./csvFiles/SpiderMainCategoryLinksDERIMOD.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row['url']
                # Change the offset value incrementally to navigate through the product list
                # You can play with the range value according to maximum product quantity
                link_urls = [url.format(i) for i in range(1, 2)]

                for link_url in link_urls:
                    print(link_url)
                    # Pass each link containing 100 products to the parse_product_pages function with the gender metadata
                    request = Request(link_url, callback=self.parse_product_pages, meta={
                                      'gender': row['gender']})
                    yield request

    def parse_product_pages(self, response):
        item = FashionwebscrapingItem()
        content = response.css('div.list-content.js-list-products')

        # Loop through the <li> elements with the "product-item" class name in the content
        for product_content in content.css('div.col-sm-4.col-xs-6.padding-lg.list-content-product-item'):
            image_urls = []

            # Get the product details and populate the items
            item['productId'] = product_content.css(
                'div.js-product-wrapper::attr(data-sku)').get()
            item['productName'] = product_content.css(
                'span.product-name::text').get()
            item['priceOriginal'] = product_content.css(
                'span.product-sale-price-list::text').get()
            item['priceSale'] = product_content.css(
                'div.basket__offer--discount::text').get(default='')

            if item['priceOriginal'] is None:
                item['priceOriginal'] = item['priceSale']

            item['imageLink'] = product_content.css('img::attr(src)').get()
            item['productLink'] = "https://www.derimod.com.tr" + \
                product_content.css('a::attr(href)').get()
            item['company'] = "DERIMOD"
            item['gender'] = response.meta['gender']
            image_urls.append(item['imageLink'])
            if item['productId'] is None:
                break

            yield item
            yield ImgData(image_urls=image_urls)
