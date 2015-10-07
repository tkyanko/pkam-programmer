import xml.etree.ElementTree as ElementTree

from jan import Jan


def build_network(input_file):
    """
    Read the input file and build a network of the JANS and their
    relations.
    """
    tree = ElementTree.parse(input_file)
    root = tree.getroot()
    jans = dict()

    for child in root:
        new_jan = Jan(child.attrib['name'], child.attrib['catagory'], child.find('value').text, [name.attrib['name'] for name in child.findall("related")])
        jans[new_jan.name] = new_jan

    return jans


def print_network(network):
    """
    Print the network of Jans to the terminal.
    """
    for jan in network.items():
        print(jan[1])


if __name__ == '__main__':
    build_network()
    print_jans()
