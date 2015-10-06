import xml.etree.ElementTree as ElementTree

from jan import Jan

INPUT_FILE = 'jans.xml'

relations = dict()
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
#        jans[child.attrib['name']] = child
#        relations[child.attrib['name']] = \
#          [name.attrib['name'] for name in child.findall("related")]

    print(jans)
    for jan in jans.items():
        print(jan[1])


if __name__ == '__main__':
    build_network()
