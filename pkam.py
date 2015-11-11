import force
import importer
import networkx as nx
import os
import re
import sys

dir = os.chdir(os.path.dirname(__file__)) #Set the script directory to be cwd
JAN_NETWORK_FILE = './jans.xml'

network = dict()

keywords = [\
('\sfor\s', 'for loop'),
('\swhile\s', 'while loop'),
('\sif\s', 'if statement')
]

def context_refiner(raw_context):
    for (regex, nodename) in keywords:
        if re.search(regex, raw_context):
            return nodename


def pkam():
    global network
    network, dictionary = importer.build_network(JAN_NETWORK_FILE)

    searchvalue = context_refiner(sys.argv[1])
    print(searchvalue)

    if searchvalue != None:
        for node in list(nx.dfs_preorder_nodes(network, 'Language')):
            print(node)
            if node == searchvalue:
                network.node[searchvalue]['selected'] = 1

    force.render_network(network)


if __name__ == '__main__':
    pkam()
