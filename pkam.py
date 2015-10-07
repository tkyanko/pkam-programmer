import importer

JAN_NETWORK_FILE = 'jans.xml'

network = dict()

def pkam():
    global network
    network = importer.build_network(JAN_NETWORK_FILE)
    print(jan_finder('git'))


def jan_finder(context):
    return network[context]


if __name__ == '__main__':
    pkam()
