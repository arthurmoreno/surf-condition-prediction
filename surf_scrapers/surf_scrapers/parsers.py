import re
import unicodedata


def normalize_ascii(value):
    return unicodedata.normalize('NFKD', str(value))


def no_special_characters(text):
    if not text:
        return None
    # import ipdb; ipdb.set_trace()
    return normalize_ascii(text)


def alpha_characters_only(text):
    if not text:
        return None
    # import ipdb; ipdb.set_trace()
    return u''.join(re.findall('[a-zA-Z]+', text))