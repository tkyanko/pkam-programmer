import xml.etree.ElementTree as ElementTree

INPUT_FILE = 'jans.xml'

relations = dict()
jans = dict()


def parse():
    """
    Reads the XML file and fills the dictionaries with the JANS and their
    relations.
    """
    tree = ElementTree.parse(INPUT_FILE)
    root = tree.getroot()

    for child in root:
        jans[child.attrib['name']] = child
        relations[child.attrib['name']] = \
          [name.attrib['name'] for name in child.findall("related")]


if __name__ == '__main__':
    parse()
