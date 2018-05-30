from scrapy import Field, Item


class CondicaoItem(Item):
    estado = Field()
    pico = Field()
    condicao = Field()
