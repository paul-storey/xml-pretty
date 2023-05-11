import re
from typing import Pattern

from lxml import etree

xml_decl_regex: Pattern[str] = re.compile(r"^<\?xml\s+.*?>")

def pprint(xml: str) -> str:
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.XML(xml_decl_regex.sub("", xml), parser)
    return etree.tostring(root, pretty_print=True, encoding="unicode")
