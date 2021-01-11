import scrapy, re

class phoneSpider(scrapy.Spider):
    name = 'numbers'
    download_delay = 1
    start_urls = [
            'https://clasificados.lavoz.com.ar/avisos/casas/4273870/san-vicente-alquilo-casa',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/4272438/oputunidad-amplio-departamento-en-barrio-gueemes',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/3372666/alberdi-3-dormitorios-amplio-luminoso.html',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/4213965/alquiler-departamento-de-tres-dormitorios-nueva-cordoba',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/3660564/mts-nuevocentro-shopping.html',
 'https://clasificados.lavoz.com.ar/avisos/casas/4271279/copia-va-villa-corina-3-dormitorio-buena-zona',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/4162968/gran-departamento-en-centro-de-cordoba-3-dormitorios-calle-sarmiento-ca',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/3930205/alquilo-dpto-3-dor-av-fuerza-aerea-b%C2%BA-rosedal.html',
 'https://clasificados.lavoz.com.ar/avisos/casas/4249180/hermosa-casa-en-complejo-cerrado-3-dorm-cochera-descubierta-patio-se-acep-masc',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/4271126/alquilo-departamento-3-dorm-palmas-complejo-cerrado',
 'https://clasificados.lavoz.com.ar/avisos/casas/4273341/sucre-428-3-dormitorios-centro',
 'https://clasificados.lavoz.com.ar/avisos/casas/4271291/imperdible-casa-de-3-dorm-villa-revol',
 'https://clasificados.lavoz.com.ar/avisos/casas/4271927/hermosa-casa-en-alquiler',
 'https://clasificados.lavoz.com.ar/avisos/departamentos/4263629/2-dorm-con-escritorio-y-doble-balcon-nueva-cordoba'
 ] 
    def parse(self, response):
        wsp_link = response.css('div.col.col-12.px1.pb1 form::attr(on)').get()
        phone = re.search('phone=(.*)&', wsp_link).group(1)
        name = 'Lautaro'
        text = f'Hola, vi su anuncio en {response.url} %0D%0AMe llamo {name}, podria brindarme más detalles?'
        final_link = f"https://api.whatsapp.com/send?phone={phone}&text={text}'"
        yield {'whatsapp': final_link}

