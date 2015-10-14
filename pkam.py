import force
import importer

JAN_NETWORK_FILE = 'jans.xml'

network = dict()

def pkam():
    global network
    network, dictionary = importer.build_network(JAN_NETWORK_FILE)
    print(network.nodes())
    print(network.edges())


    force.render_network(network)



def jan_finder(context):
    return network[context]


if __name__ == '__main__':
    pkam()
