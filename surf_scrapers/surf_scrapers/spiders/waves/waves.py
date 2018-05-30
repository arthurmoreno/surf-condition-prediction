import re
from datetime import datetime

from scrapy.loader import ItemLoader
from scrapy import Spider, Request

from surf_scrapers.loaders import (CondicaoLoader, OndaLoader, VentoLoader,
                                   MareLoader, TempoLoader)
from surf_scrapers.spiders.waves.constantes import (
    XPATH_PRAIAS, XPATH_PICO, XPATH_ONDAS,
    XPATH_VENTOS, XPATH_MARE, XPATH_TEMPO
)


class WavesSpider(Spider):
    name = "waves"

    def start_requests(self):
        estados = [
            # 'bahia',
            # 'sergipe',
            'alagoas',
            # 'pernambuco',
            # 'paraiba',
            # 'rio-grande-do-norte'
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

        formacao_raw = response.xpath(XPATH_ONDAS['formacao']).extract_first()
        if '(' in formacao_raw:
            status = re.findall(XPATH_ONDAS['formacao_regex'], formacao_raw)

        loader = CondicaoLoader(response=response)
        loader.add_value('status', status)

        loader.add_value('estado', meta['estado'])
        loader.add_value('pico', meta['pico'])
        loader.add_value('dia', datetime.now().date().strftime("%Y-%m-%d"))

        loader.add_value('onda', self.extract_onda(
            response=response, formacao_raw=formacao_raw))
        loader.add_value('vento', self.extract_vento(response=response))
        loader.add_value('mare', self.extract_mare(response=response))
        loader.add_value('tempo', self.extract_tempo(response=response))

        return loader.load_item()

    def extract_onda(self, response, formacao_raw=None):
        loader = OndaLoader(response=response)

        loader.add_xpath('tamanho', XPATH_ONDAS['tamanho'])
        loader.add_xpath('direcao', XPATH_ONDAS['direcao'])
        if formacao_raw:
            loader.add_value('formacao', formacao_raw)

        return loader.load_item()
        
    def extract_vento(self, response):
        loader = VentoLoader(response=response)

        loader.add_xpath('direcao', XPATH_VENTOS['direcao'])
        loader.add_xpath('intensidade', XPATH_VENTOS['intensidade'])
        loader.add_xpath('velocidade', XPATH_VENTOS['velocidade'])

        return loader.load_item()
        
    def extract_mare(self, response):
        loader = MareLoader(response=response)

        loader.add_xpath('seca', XPATH_MARE['seca'])
        loader.add_xpath('cheia', XPATH_MARE['cheia'])
        loader.add_xpath('lua', XPATH_MARE['lua'])

        return loader.load_item()
        
    def extract_tempo(self, response):
        loader = TempoLoader(response=response)

        loader.add_xpath('previsao', XPATH_TEMPO['previsao'])
        loader.add_xpath('agua', XPATH_TEMPO['agua'])
        loader.add_xpath('indice', XPATH_TEMPO['indice'])

        return loader.load_item()
