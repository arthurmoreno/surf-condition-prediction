from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from surf_scrapers import processors
from surf_scrapers.items import (CondicaoItem, OndaItem, VentoItem,
                                 MareItem, TempoItem)

class OndaLoader(ItemLoader):
    default_item_class = OndaItem

    tamanho_in = processors.clean_characters()
    direcao_in = processors.clean_characters()
    formacao_in = processors.clean_characters()
    
    tamanho_out = TakeFirst()
    direcao_out = TakeFirst()
    formacao_out = TakeFirst()


class VentoLoader(ItemLoader):
    default_item_class = VentoItem

    direcao_in = processors.clean_characters()
    intensidade_in = processors.clean_characters()
    velocidade_in = processors.clean_characters()

    direcao_out = TakeFirst()
    intensidade_out = TakeFirst()
    velocidade_out = TakeFirst()


class MareLoader(ItemLoader):
    default_item_class = MareItem

    seca_in = processors.clean_characters()
    cheia_in = processors.clean_characters()
    lua_in = processors.clean_characters()

    seca_out = TakeFirst()
    cheia_out = TakeFirst()
    lua_out = TakeFirst()


class TempoLoader(ItemLoader):
    default_item_class = TempoItem

    seca_in = processors.clean_characters()
    cheia_in = processors.clean_characters()
    lua_in = processors.clean_characters()

    seca_out = TakeFirst()
    cheia_out = TakeFirst()
    lua_out = TakeFirst()


class CondicaoLoader(ItemLoader):
    default_item_class = CondicaoItem

    pico_in = processors.clean_characters()
    status_in = processors.clean_characters()

    estado_out = TakeFirst()
    pico_out = TakeFirst()
    status_out = TakeFirst()
    dia_out = TakeFirst()
