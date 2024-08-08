
import scrapy

class FullContentSpider(scrapy.Spider):
    name = "full_content"
    start_urls = [
        'https://spiderum.com/bai-dang/Cam-nang-chong-soc-khi-nhap-ngu-dKqhAzT0rEE4',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            })

    def parse(self, response):
        # Extract the full HTML content of the page
        full_html = response.text
        
        # Optionally extract specific parts if needed
        scripts = response.css('script::text').getall()
        styles = response.css('style::text').getall()

        yield {
            'full_html': full_html,
            'scripts': scripts,
            'styles': styles
        }
