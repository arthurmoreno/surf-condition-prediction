from datetime import datetime

from scrapy.loader import ItemLoader
from scrapy import Spider, Request

from surf_scrapers.loaders import CondicaoLoader


XPATH_PRAIAS = '//table[@id="table_ws"]//tr//a'
XPATH_CONDICAO = '//tr/td/b[contains(text(),"Forma")]/../../td[2]/div[2]/text()'

XPATH_PICO = {
    'nome': './text()',
    'url': './@href'
}


class WavesSpider(Spider):
    name = "waves"

    def start_requests(self):
        estados = [
            'bahia',
            'sergipe',
            'alagoas',
            'pernambuco',
            'paraiba',
            'rio-grande-do-norte'
        ]
        urls = {
            estado: 'http://www.waves.com.br/surf/ondas/condicao/{}/'.format(estado)
            for estado in estados
        }

        for estado, url in urls.items():
            meta = {'estado': estado}
            yield Request(
                url=url,
                meta=meta,
                callback=self.consultar_picos
            )

    def consultar_picos(self, response):
        picos = response.xpath(XPATH_PRAIAS)

        for pico in picos:
            meta = response.meta.copy()
            meta['pico'] = pico.xpath(XPATH_PICO['nome']).extract_first()
            pico_url = pico.xpath(XPATH_PICO['url']).extract_first()
            yield Request(
                url=pico_url,
                meta=meta,
                callback=self.parse_condicao
            )

    def parse_condicao(self, response):
        meta = response.meta.copy()

        loader = CondicaoLoader(response=response)
        loader.add_xpath('condicao', XPATH_CONDICAO)
        loader.add_value('estado', meta['estado'])
        loader.add_value('pico', meta['pico'])
        loader.add_value('dia', datetime.now().date().strftime("%Y-%m-%d"))
        return loader.load_item()