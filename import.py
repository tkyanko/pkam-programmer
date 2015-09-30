import xml.etree.ElementTree as ElementTree

INPUT_FILE = 'jans.xml'

relations = dict()
jans = dict()

def parse():
    tree = ElementTree.parse(INPUT_FILE)
    root = tree.getroot()

    for child in root:
        jans[child.attrib['name']] = child

    print(jans)


if __name__ == '__main__':
    parse()
