def build_model_coordinates(data):
    return list(zip(data["x_indices"], data["y_indices"], data["z_indices"]))


def get_block_minerals(minerals, mineral_names, block_number):
    block_minerals = {}
    for index, mineral_name in enumerate(mineral_names):
        block_minerals[mineral_name] = minerals[index][0][block_number]
    return block_minerals
