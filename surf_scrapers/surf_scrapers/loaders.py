from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from surf_scrapers.items import CondicaoItem
from surf_scrapers import processors


class CondicaoLoader(ItemLoader):
    default_item_class = CondicaoItem

    pico_in = processors.clean_characters()
    condicao_in = processors.clean_characters()

    estado_out = TakeFirst()
    pico_out = TakeFirst()
    condicao_out = TakeFirst()
