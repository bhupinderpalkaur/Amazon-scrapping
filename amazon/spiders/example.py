# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem


class AmazonProductSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["amazon.com"]

    # Use working product URL below
    start_urls = [
        "https://www.amazon.in/Atomic-Habits-Proven-Build-Break-ebook/dp/B01N5AX61W/ref=pd_sim_351_7?_encoding=UTF8&pd_rd_i=B01N5AX61W&pd_rd_r=8d2e4820-e67c-486a-b361-70b9680b2cf1&pd_rd_w=hdiaX&pd_rd_wg=NnyGj&pf_rd_p=2d36b700-09c8-4bd0-9799-a8dbde5e27f5&pf_rd_r=STBCD827GYKMVG4G7Z1N&psc=1&refRID=STBCD827GYKMVG4G7Z1N",
        "https://www.amazon.in/Power-Your-Subconscious-Mind-ebook/dp/B07PJVJCQD/ref=sr_1_3?dchild=1&keywords=best+books&qid=1585289971&sr=8-3",
        "https://www.amazon.in/Percy-Jackson-Monsters-Rick-Riordan/dp/0141346841/ref=sr_1_1?dchild=1&keywords=best+books&qid=1585289971&sr=8-1",
        "https://www.amazon.in/Death-Inside-Story-those-shall/dp/0143450832/ref=sr_1_4?dchild=1&keywords=books&qid=1585290073&refinements=p_n_binding_browse-bin%3A1318376031&rnid=1318374031&s=books&sr=1-4"
    ]

def parse(self, response):
    items = AmazonItem()

    title = response.xpath('//h1[@id="title"]/span/text()').extract()
    sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
    category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
    availability = response.xpath('//div[@id="availability"]//text()').extract()
    items['product_name'] = ''.join(title).strip()
    items['product_sale_price'] = ''.join(sale_price).strip()
    items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
    items['product_availability'] = ''.join(availability).strip()
    yield items