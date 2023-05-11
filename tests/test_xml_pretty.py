from io import BytesIO
from xml_pretty import pprint

def test_basic() -> None:
    xml_in: str = "<?xml encoding=\"utf-8\"?><a><b><c>text</c></b></a>"
    expected: str = """<a>
  <b>
    <c>text</c>
  </b>
</a>
"""
    actual: str = pprint(xml_in)
    assert actual == expected
