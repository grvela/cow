import scrapy 

class WhatsappSpider(scrapy.Spider):
    name = "whatsapp"

    def start_requests(self):
        url = ['http://web.whatsapp.com']
        yield scrapy.Request(url= url, callback=self.parse)

    def parse(self, response):
        pass