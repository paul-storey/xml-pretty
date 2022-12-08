from io import BytesIO
from xml_pretty import __version__, pprint

def test_version():
    assert __version__ == '0.1.0'

def test_basic() -> None:
    xml_in: str = "<a><b><c>text</c></b></a>"
    expected: str = """<a>
  <b>
    <c>text</c>
  </b>
</a>
"""
    actual: str = pprint(xml_in)
    assert actual == expected
