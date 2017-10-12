"""Functions to produce font metrics"""
from collections import namedtuple

def glyph_metrics(font, glyph):
    lsb = _glyph_lsb(font, glyph)
    rsb = _glyph_rsb(font, glyph)
    adv = _glyph_adv_width(font, glyph)
    return _GlyphMetrics(glyph, lsb, rsb, adv)


def font_glyph_metrics(font):
    glyphs = font.getGlyphSet().keys()
    return [glyph_metrics(font, g) for g in glyphs]


_GlyphMetrics = namedtuple('GlyphMetrics', ['glyph', 'lsb', 'rsb', 'adv'])


def _glyph_adv_width(font, glyph):
    return font['hmtx'][glyph][0]


def _glyph_lsb(font, glyph):
    """Get the left side bearing for a glyph.
    If the Xmin attribute does not exist, the font is zero width so
    return 0"""
    try:
        return font['glyf'][glyph].xMin
    except AttributeError:
        return 0


def _glyph_rsb(font, glyph):
    """Get the right side bearing for a glyph.
    If the Xmax attribute does not exist, the font is zero width so
    return 0"""
    glyph_width = font['hmtx'].metrics[glyph][0]
    try:
        return glyph_width - font['glyf'][glyph].xMax
    except AttributeError:
        return 0

