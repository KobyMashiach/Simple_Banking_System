class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        self.height /= 0.3048
        return self.height
