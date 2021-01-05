import scrapy, re


class ClasificadosSpider(scrapy.Spider):
    name = 'clasificados'
    download_delay = 1
    start_urls = ['https://clasificados.lavoz.com.ar/inmuebles/todo/?cantidad-de-dormitorios[0]=3-dormitorios&operacion=alquileres&provincia=cordoba&ciudad=cordoba&precio-hasta=30000&moneda=pesos']

    def parse(self, response):
        product_links = response.css('div.col.col-12.mx1.md-mx0.md-mr1.bg-white.mb2.line-height-3.card.relative.safari-card a::attr(href)')
        yield from response.follow_all(product_links, self.parse_product)

        #self.scraped_pages = 0
        #if self.scraped_pages <= 5:
        next_page = response.css('div.wrapper.py2 a.right.button-narrow::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            with open('fail.html', 'wb') as f:
                f.write(response.body)

    def parse_product(self, response):
        description = '\n'.join([data.get().strip() for data in response.css('div.container.px1.md-px0.h4 *::text')]).lower()
        town = response.css('div.col.col-12.md-pt2 *::text') 
        seller = response.css('div.col.col-8.pt1 h4.m0::text').get()
        expenses = response.css('h3.h4.mt0.main.bolder::text').get()
        if not expenses:
            try:
                expenses = re.search(r'.*expensas.*', description).group(),
            except:
                expenses = ''

        try:
            warranty = re.search(r'.*garant(i|í)a(s)?.*', description).group(),
        except:
            warranty = ''

        yield {
            'title': response.css('h1.h2.m0.mb0.bolder.line-height-1::text').get(),
            'price': response.css('div.h2.mt0.main.bolder::text').get(),
            'direction': ' '.join([data.get().strip() for data in town])[11:].strip(),
            'seller': seller.strip() if seller else '',
            'expenses': expenses if expenses else '',
            'warranty': warranty if warranty else '',
        }


