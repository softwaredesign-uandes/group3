class Block:
    x_index = None
    y_index = None
    z_index = None
    weight = None
    minerals = None

    def __init__(self, x, y, z, weight, minerals):
        self.x_index = x
        self.y_index = y
        self.z_index = z
        self.weight = weight
        self.minerals = minerals

    def id(self, max_x, max_y):
        return (self.z_index * max_x * max_y) + (self.y_index * max_x) + self.x_index
