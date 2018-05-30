from scrapy.loader import processors
from w3lib.html import remove_tags

from surf_scrapers import parsers


def clean_characters():
    return processors.MapCompose(
        remove_tags,
        str.strip,
        parsers.no_special_characters,
        parsers.alpha_characters_only)
