def build_model_coordinates(data):
    return list(zip(data["x_indices"], data["y_indices"], data["z_indices"]))


def get_block_minerals(minerals, mineral_names, block_number):
    block_minerals = {}
    for index, mineral_name in enumerate(mineral_names):
        block_minerals[mineral_name] = minerals[index][0][block_number]
    return block_minerals


def add_to_mineral_deposits_if_new(mineral_deposits, mineral_deposit):
    if mineral_deposit not in mineral_deposits.keys():
        mineral_deposits[mineral_deposit] = {
            'name': mineral_deposit,
            'id': len(mineral_deposits.keys()),
            'block_models': []
        }
    return mineral_deposits[mineral_deposit]['id']


def add_to_mineral_deposits_dict(mineral_deposits, mineral_deposit, block_model_id):
    add_to_mineral_deposits_if_new(mineral_deposits, mineral_deposit)
    mineral_deposits[mineral_deposit]['block_models'].append(block_model_id)
