import scrapy

class marsScraper(scrapy.Spider):
    name = 'mars'

    def start_requests(self):
        start_urls = [
            'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        ]

    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url
        filename = 'mars.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    
   