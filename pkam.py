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
('\sif\s', 'if statement'),
('\sthread\s', 'threading module')
]

def context_refiner(raw_context):
    nodename = None
    for (regex, nodename) in keywords:
        if re.search(regex, raw_context):
            return nodename


def pkam():
    global network
    network, dictionary = importer.build_network(JAN_NETWORK_FILE)

    if sys.argv[1] == 'find':
        searchvalue = context_refiner(sys.argv[2])
        context = 'Unknown'

        if searchvalue != None:
            for node in list(nx.dfs_preorder_nodes(network, 'Language')):
                if node == searchvalue:
                    context = network.node[searchvalue]['name']

        print(context)

    elif sys.argv[1] == 'show':
        searchvalue = context_refiner(sys.argv[2])

        if searchvalue != None:
            for node in list(nx.dfs_preorder_nodes(network, 'Language')):
                if node == searchvalue:
                    context = network.node[searchvalue]['selected'] = 1
            force.render_network(network)


if __name__ == '__main__':
    pkam()
