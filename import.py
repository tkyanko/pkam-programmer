import xml.etree.ElementTree as ElementTree

INPUT_FILE = 'jans.xml'

def parse():
    tree = ElementTree.parse(INPUT_FILE)


if __name__ == '__main__':
    parse()
