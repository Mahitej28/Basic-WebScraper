import scrapy 

class ChocolatespiderSpider(scrapy.Spider):

    #the name of the spider
    name = 'chocolatespider'

    #the url of the first page that we will start scraping
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response):

        #here we are looping through the products and extracting the name, price & url
        products = response.css('product-item')
        for product in products:
            #here we put the data returned into the format we want to output for our csv or json file
            yield{
                'name' : product.css('a.product-item-meta__title::text').get(),
                'price' : product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>',''),
                'url' : product.css('div.product-item-meta a').attrib['href'],
            }