class Jan(object):
    def __init__(self, name, catagory, value, relations):
        self.name = name
        self.catagory = catagory
        self.value = value
        self.relations = relations

    def __str__(self):
        return 'Name: {self.name!s}, Catagory: {self.catagory!s}, Value: {self.value!s}, Relations: {self.relations!s}'.format(**locals())
