import operator
from functools import reduce


class BlockModel:
    blocks = None

    def __init__(self):
        self.blocks = []

    def insert_block(self, block):
        self.blocks.append(block)

    def replace_blocks(self, blocks):
        self.blocks = blocks

    def total_weight(self):
        return sum(map(
            lambda block: block.weight,
            self.blocks
        ))

    def num_blocks(self):
        return len(self.blocks)

    def mineral_weight(self):
        block_minerals = list(map(
            lambda block: block.minerals,
            self.blocks
        ))
        all_mineral_names = reduce(operator.or_, (d.keys() for d in block_minerals))
        minerals = {key: [d.get(key) for d in block_minerals] for key in all_mineral_names}
        for key in minerals.keys():
            minerals[key] = sum(minerals[key])
        return minerals

    def get_block_id(self, block):
        max_x = max(list(map(lambda m_block: block.x_index, self.blocks)))
        max_y = max(list(map(lambda m_block: block.y_index, self.blocks)))
        return block.id(max_x, max_y)

    def get_block_by_id(self, id):
        blocks_by_id = dict()
        for block in self.blocks:
            blocks_by_id[self.get_block_id(block)] = block
        if id not in blocks_by_id.keys():
            return None
        return blocks_by_id[id]

