


XPATH_PRAIAS = '//table[@id="table_ws"]//tr//a'

XPATH_PICO = {
    'nome': './text()',
    'url': './@href'
}

DIV_PATTERN = '//h4/span[contains(text(),"{}")]/../..//tr/td/b[contains(text(),'

ONDAS = DIV_PATTERN.format('ONDAS')

XPATH_ONDAS = {
    'tamanho': '{}"Tamanho")]/../../td[2]/span/text()'.format(ONDAS),
    'direcao': '{}"Dire")]/../../td[2]'.format(ONDAS),
    'formacao': '{}"Forma")]/../../td[2]/div[2]/text()'.format(ONDAS),
    'formacao_regex': r'\(([^()]+)\)'
}

VENTO = DIV_PATTERN.format('VENTO')

XPATH_VENTOS = {
    'direcao': '{}"Dire")]/../../td[2]'.format(VENTO),
    'intensidade': '{}"Intensidade")]/../../td[2]'.format(VENTO),
    'velocidade': '{}"Velocidade")]/../../td[2]'.format(VENTO)
}

MARE = DIV_PATTERN.format('MARE')

XPATH_MARE = {
    'seca': '{}"Seca")]/../../td[2]'.format(MARE),
    'cheia': '{}"Cheia")]/../../td[2]'.format(MARE),
    'lua': '{}"Lua")]/../../td[2]'.format(MARE)
}

TEMPO = DIV_PATTERN.format('TEMPO')

XPATH_TEMPO = {
    'previsao': '{}"Seca")]/../../td[2]'.format(TEMPO),
    'agua': '{}"gua")]/../../td[2]'.format(TEMPO),
    'indice': '{}"ndice")]/../../td[2]'.format(TEMPO)
}
