from scrapy import Field, Item

class OndaItem(Item):
    tamanho = Field()
    direcao = Field()
    formacao = Field()

class VentoItem(Item):
    direcao = Field()
    intensidade = Field()
    velocidade = Field()

class MareItem(Item):
    seca = Field()
    cheia = Field()
    lua = Field()

class TempoItem(Item):
    previsao = Field()
    agua = Field()
    indice = Field()

class CondicaoItem(Item):
    estado = Field()
    pico = Field()
    dia = Field()

    status = Field()

    onda = Field()
    vento = Field()
    mare = Field()
    tempo = Field()
