import scrapy
class NewSpider(scrapy.Spider):
    name ="new_spider"
    start_urls = ['http://172.18.58.238/creative/']
    def parse(self, response):
                css_selector = 'img'
                for x in response.css(css_selector):
                            newsel = '@src'
                            yield {
                                'Image Link': x.xpath(newsel).extract_first(),
                            }

# Display Reference Webpage
class References(scrapy.Spider):
    name = "Display References"
    start_urls = ['http://172.18.58.238/creative/']
# Create references.json in directory
    open("Output References\\references.json", 'w').close()

    def parse(self, response):
# Open references.json folder and append its results into references.json
        test = open("Output References\\references.json", 'a')
        for link in response.css('a'):
            link_results = link.css('a::attr(href)').get()
            test.write(str({'References': link_results}) + "\n")
        test.close()

#To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
                )