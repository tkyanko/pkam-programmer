import xml.etree.ElementTree as ElementTree

from jan import Jan

INPUT_FILE = 'jans.xml'

jans = dict()


def build_network():
    """
    Reads the XML file and fills the dictionaries with the JANS and their
    relations.
    """
    tree = ElementTree.parse(INPUT_FILE)
    root = tree.getroot()

    for child in root:
        new_jan = Jan(child.attrib['name'], child.attrib['catagory'], child.find('value').text, [name.attrib['name'] for name in child.findall("related")])
        jans[new_jan.name] = new_jan


def print_jans():
    """
    Prints the network of Jans to the terminal.
    """
    for jan in jans.items():
        print(jan[1])


if __name__ == '__main__':
    build_network()
