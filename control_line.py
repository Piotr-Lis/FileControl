class ControlLine:

    def __init__(self):
        self.controlers = []

    def __iter__(self):
        return iter(self.controlers)

    def add_controler(self, controler):
        self.controlers.append(controler)
