class VizState:
    def __init__(self, values):
        self.values = values.copy
        self.highlights = set()
        self.pointers = {}