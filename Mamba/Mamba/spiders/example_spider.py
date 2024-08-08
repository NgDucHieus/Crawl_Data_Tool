import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = [
        'https://spiderum.com/bai-dang/Cam-nang-chong-soc-khi-nhap-ngu-dKqhAzT0rEE4',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            })

    def parse(self, response):
        if response.status == 403:
            self.logger.info(f'403 Forbidden: {response.url}')
        else:
            title = response.css('title::text').get()
            description = response.css('div.description p::text').getall()
            content = response.css('div.post-body::text').getall()
            yield {
                'title': title,
                'content': content,
                'description': description
            }