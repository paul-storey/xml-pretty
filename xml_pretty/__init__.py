from typing import BinaryIO
from lxml import etree

__version__ = '0.1.0'

def pprint(xml: str) -> str:
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.XML(xml, parser)
    return etree.tostring(root, pretty_print=True, encoding="unicode")
