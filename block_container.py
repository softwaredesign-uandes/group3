from functools import reduce


class BlockContainer:
    x_index = None
    y_index = None
    z_index = None
    blocks = None

    def __init__(self, block):
        self.x_index = block.x_index
        self.y_index = block.y_index
        self.z_index = block.z_index
        self.blocks = [block]

    def __dict__(self):
        return dict(
            x_index=self.x_index,
            y_index=self.y_index,
            z_index=self.z_index,
            weight=self.weight,
            grades=self.minerals
        )

    def id(self, max_x, max_y):
        return (self.z_index * max_x * max_y) + (self.y_index * max_x) + self.x_index

    def join_blocks(self, block_container_list):
        self.blocks += reduce(lambda bc1, bc2: bc1.blocks + bc2.blocks, block_container_list)
        return self
    
    @property
    def weight(self):
        return sum(map(
            lambda block: block.weight,
            self.blocks
        ))
    
    @property
    def minerals(self):
        minerals = {}
        total_weight = self.weight
        total_weight = total_weight if total_weight > 0 else 1
        for block in self.blocks:
            for mineral in block.minerals:
                if mineral not in minerals.keys():
                    minerals[mineral] = 0
                ponderator = block.weight / total_weight
                minerals[mineral] += block.minerals[mineral] * ponderator
        return minerals