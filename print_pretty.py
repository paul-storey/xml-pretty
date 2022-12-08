import fileinput
from xml_pretty import pprint

if __name__ == "__main__":
    buffer: str = ""
    for line in fileinput.input():
        buffer += line
    print(pprint(buffer))
