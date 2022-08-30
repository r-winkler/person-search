class Repository(object):
    def __init__(self, adapter=None):
        if not adapter:
            raise ValueError("Invalid repository implementation")
        self.client = adapter()

    def find_all(self):
        return self.client.find_all()

