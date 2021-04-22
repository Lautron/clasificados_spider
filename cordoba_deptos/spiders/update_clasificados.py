import scrapy, re, csv


class ClasificadosSpider(scrapy.Spider):
    name = 'update_clas'
    download_delay = 1
    start_urls = ['https://clasificados.lavoz.com.ar/inmuebles/todo/?cantidad-de-dormitorios[0]=3-dormitorios&operacion=alquileres&provincia=cordoba&ciudad=cordoba&precio-hasta=30000&moneda=pesos']
    present_urls = { 
        data[1] for data in csv.reader(
            open('/home/lautarob/Documents/code/web-scraping/cordoba/cordoba_deptos/miguel.csv', 'r')
            ) 
        }

    def parse(self, response):
        product_links = response.css('div.col.col-12.mx1.md-mx0.md-mr1.bg-white.mb2.line-height-3.card.relative.safari-card a::attr(href)')
        for item in product_links:
            if item.get() not in self.present_urls and 'avisos' in item.get():
                yield response.follow(item, self.parse_product)

        next_page = response.css('div.wrapper.py2 a.right.button-narrow::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            print('No next page available')
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
            #'title': response.css('h1.h2.m0.mb0.bolder.line-height-1::text').get(),
            'url': response.url,
            'price': response.css('div.h2.mt0.main.bolder::text').get(),
            'empty_field': '',
            'empty_field2': '',
            'direction': ' '.join([data.get().strip() for data in town])[11:].strip(),
            'expenses': expenses if expenses else '',
            'seller': seller.strip() if seller else '',
            'warranty': warranty if warranty else '',
        }


