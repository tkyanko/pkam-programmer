import force
import importer
import os
import re
import sys

dir = os.chdir(os.path.dirname(__file__)) #Set the script directory to be cwd
JAN_NETWORK_FILE = './jans.xml'

network = dict()


def context_refiner(raw_context):
    x = re.search('\sfor\s', raw_context) for 
    return x


def pkam():
    global network
    network, dictionary = importer.build_network(JAN_NETWORK_FILE)

    print(context_refiner(sys.argv[1]))

    force.render_network(network)


if __name__ == '__main__':
    pkam()
