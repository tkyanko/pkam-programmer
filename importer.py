import networkx as nx
import xml.etree.ElementTree as ElementTree
import matplotlib.pyplot as plt

from jan import Jan


def build_network(input_file):
    """
    Read the input file and build a network and dict of the JANS and their
    relations.
    """
    tree = ElementTree.parse(input_file)
    root = tree.getroot()
    jan_graph = nx.Graph()
    jan_dict = dict()

    for child in root:
        new_jan = Jan(child.attrib['name'], child.attrib['catagory'], child.find('value').text, [name.attrib['name'] for name in child.findall("related")])
        jan_dict[new_jan.name] = new_jan

    #Adding Jans as nodes
    for name in jan_dict.keys():
        jan_graph.add_node(name)
        jan_graph.node[name]['name'] = name

    for jan in jan_dict.values():
        for related in jan.relations:
            jan_graph.add_edge(jan.name, related)
        jan_graph.node[jan.name]['url'] = jan.value
        jan_graph.node[jan.name]['selected'] = '0'

    return jan_graph, jan_dict


def print_network(network):
    """
    Print the network of Jans to the terminal.
    """
    for jan in network.items():
        print(jan[1])


if __name__ == '__main__':
    build_network()
    print_jans()
