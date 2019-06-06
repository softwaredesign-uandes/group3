import decimal
from functools import reduce
from itertools import product


def check_row(dictionary, index):
    if index not in dictionary.keys():
        dictionary[index] = {}
    return


def get_block(block_model, x, y, z, units_keys):
    x = str(x)
    y = str(y)
    z = str(z)

    zero_minerals = dict([(unit_key, 0) for unit_key in units_keys])
    air_block = {'weight': 0, 'minerals': zero_minerals}
    if x not in block_model.keys():
        return air_block
    if y not in block_model[x].keys():
        return air_block
    if z not in block_model[x][y].keys():
        return air_block
    return block_model[x][y][z]


def get_valid_steps(max_value, reblock_size):
    valid_x_references = filter(lambda x: x <= max_value, map(lambda x: x * reblock_size, range(0, max_value + 1)))
    return list(valid_x_references)


def get_blocks_from_reference_until_stop(model, start_reference, step_references, units):

    x_start_index, y_start_index, z_start_index = start_reference[0], start_reference[1], start_reference[2]

    x_end_index, y_end_index, z_end_index = x_start_index + step_references[0], y_start_index + step_references[1], z_start_index + step_references[2]

    # increase the end index by 1 to include itself
    valid_x_indexes = range(x_start_index, x_end_index)
    valid_y_indexes = range(y_start_index, y_end_index)
    valid_z_indexes = range(z_start_index, z_end_index)

    indexes_for_required_blocks = product(valid_x_indexes, valid_y_indexes, valid_z_indexes)
    blocks_from_reference_until_stop = map(lambda index: get_block(model,index[0],index[1],index[2],units.keys()),indexes_for_required_blocks)

    return blocks_from_reference_until_stop


def get_mineral(block, mineral_name):
    return decimal.decimal.Decimal(block['minerals'][mineral_name])


def transform_blocks_batch_to_one_block(blocks, units):
    total_weight = sum(map(lambda block: get_block_weight(block),blocks))
    blocks = list(blocks)
    mineral_names = units.keys()
    total_minerals = {}

    for mineral_name in mineral_names:
        total_mineral = sum(map(lambda block: get_mineral(block, mineral_name), blocks))
        mineral_count = len(list(filter(lambda block: get_mineral(block, mineral_name) > 0,blocks)))
        average_mineral = total_mineral/mineral_count if mineral_count>0 else 0
        total_minerals[mineral_name] = str(average_mineral)

    new_block = {'weight': str(total_weight), 'minerals': total_minerals}
    return new_block



def reblock(blocks, reblock_size_x, reblock_size_in_y, reblock_size_in_z, units):
    x_max, y_max, z_max = get_max_coords_of_model(blocks)
    reblock_size = [reblock_size_x, reblock_size_in_y, reblock_size_in_z]
    valid_x_steps = get_valid_steps(x_max, reblock_size_x)
    valid_y_steps = get_valid_steps(y_max, reblock_size_in_y)
    valid_z_steps = get_valid_steps(z_max, reblock_size_in_z)

    x_new_block_indexes = map(lambda x: str(x), range(0, len(valid_x_steps)))
    y_new_block_indexes = map(lambda y: str(y), range(0, len(valid_y_steps)))
    z_new_block_indexes = map(lambda z: str(z), range(0, len(valid_z_steps)))

    new_block_indexes = product(x_new_block_indexes, y_new_block_indexes, z_new_block_indexes)
    references_to_reblock = product(valid_x_steps, valid_y_steps, valid_z_steps)
    block_batches = list(map(lambda reference: list(get_blocks_from_reference_until_stop(blocks, reference, reblock_size, units)),references_to_reblock))

    batches_reblocked = list(map(lambda block_batch: transform_blocks_batch_to_one_block(block_batch, units), block_batches))

    new_blocks = {}
    new_indexes_and_batches_reblocked = list(zip(new_block_indexes, batches_reblocked))
    for new_index_and_batch_reblocked in new_indexes_and_batches_reblocked:
        coord = new_index_and_batch_reblocked[0]
        x = coord[0]
        y = coord[1]
        z = coord[2]
        coordinates = {'x': x, 'y': y, 'z': z}
        insert_into_blocks(new_blocks, new_index_and_batch_reblocked[1], coordinates)
    return new_blocks


def insert_into_blocks(blocks, block, coordinates):
    check_row(blocks, coordinates['x'])
    check_row(blocks[coordinates['x']], coordinates['y'])
    check_row(blocks[coordinates['x']][coordinates['y']], coordinates['z'])
    blocks[coordinates['x']][coordinates['y']][coordinates['z']] = block


def get_portion(block_weight, mineral_weight, unit):
    block_weight = decimal.decimal.Decimal(block_weight)
    mineral_weight = decimal.decimal.Decimal(mineral_weight)
    if unit == '%':
        return block_weight * mineral_weight / 100
    elif unit == 'ppm':
        return block_weight * mineral_weight / 1000000


def get_maximum_from_string_array(string_array):

    max_value = reduce(lambda number_string, max_value_string: max(int(number_string), int(max_value_string)),
                       string_array)
    return max_value


def get_max_coords_of_model(model):


    possible_triple_keys_in_model = get_triples_keys_from_dictionaries_tree(model)
    x_keys  = map (lambda triple: triple[0],possible_triple_keys_in_model)
    maximum_x_key = get_maximum_from_string_array(x_keys)
    y_keys = map(lambda triple: triple[1], possible_triple_keys_in_model)
    maximum_y_key = get_maximum_from_string_array(y_keys)

    z_keys = map(lambda triple: triple[2], possible_triple_keys_in_model)
    maximum_z_key = get_maximum_from_string_array(z_keys)

    return maximum_x_key, maximum_y_key, maximum_z_key

    x_keys = model.keys() + [default_max_value]
    maximum_x_key = get_maximum_from_string_array(x_keys)
    y_keys = reduce(lambda y_keys_for_x, total_y_keys: y_keys_for_x + total_y_keys,
                    map(lambda x_key: list(model[x_key].keys()), model.keys()))

    maximum_y_key = get_maximum_from_string_array(y_keys)
    z_keys = map(lambda triple: triple[2], get_triples_keys_from_dictionaries_tree(model))
    z_keys.append(default_max_value)
    maximum_z_key = get_maximum_from_string_array(z_keys)

    return maximum_x_key, maximum_y_key, maximum_z_key


def load_file(file_name):
    input_file = open(file_name, 'r')
    blocks_as_list_of_parameters = []
    for line in input_file:
        block_as_list_of_parameters = line.strip().split(' ')
        blocks_as_list_of_parameters.append(block_as_list_of_parameters)
    input_file.close()
    return blocks_as_list_of_parameters


def create_blocks_model(blocks_as_list_of_parameters, coordinates, ores, weight):
    blocks = {}
    for block_as_list_of_parameters in blocks_as_list_of_parameters:
        block_coords = {
            'x': block_as_list_of_parameters[coordinates['x']],
            'y': block_as_list_of_parameters[coordinates['y']],
            'z': block_as_list_of_parameters[coordinates['z']]
        }

        block_minerals = {}
        for mineral in ores.keys():
            block_minerals[mineral] = block_as_list_of_parameters[ores[mineral]]
        block_weight = block_as_list_of_parameters[weight]
        block = dict(minerals=block_minerals, weight=block_weight)
        insert_into_blocks(blocks, block, block_coords)
    return blocks


def load_file_menu():
    file_name = input('Enter the file name: ')
    coordinates = {}
    ores = {}
    coordinates['x'] = int(input('Enter the position of the x coordinate: '))
    coordinates['y'] = int(input('Enter the position of the y coordinate: '))
    coordinates['z'] = int(input('Enter the position of the z coordinate: '))
    weight = int(input('Enter the position of the weight parameter: '))
    number_of_ores = int(input('Enter the quantity of ores for the blocks: '))
    units = {}
    for ore in range(number_of_ores):
        ore_name = input('Enter the name for the ore: ')
        ores[ore_name] = int(input('Enter the coordinate for the ore: '))
        units[ore_name] = input('Enter the units for the ore (ppm or %):')
    return file_name, coordinates, weight, ores, units


def show_block_info(block, units):
    print('')
    print('Block info: ')
    print('Weight\t:', block['weight'])
    if (block['minerals']):

        for mineral in block['minerals'].keys():
            print(mineral, '\t:', block['minerals'][mineral], units[mineral])


def get_block_mineral_weight(block, units):
    block_weight = get_block_weight(block)
    mineral_keys = block['minerals'].keys()
    mineral_weights = map(
        lambda mineral_key: get_portion(block_weight, block['minerals'][mineral_key], units[mineral_key]), mineral_keys)
    total_mineral_weight = sum(mineral_weights)

    return total_mineral_weight


def get_block_weight(block):
    if 'weight' not in block.keys():
        return 0
    block_weight = decimal.Decimal(block['weight'])
    return block_weight


def get_leaf_values_from_dictionaries_tree(blocks):
    triples_keys = get_triples_keys_from_dictionaries_tree(blocks)
    all_blocks = list(map(lambda triple: blocks[triple[0]][triple[1]][triple[2]], triples_keys))
    return all_blocks


def get_triples_keys_from_dictionaries_tree(dictionaries_tree):

    default_triples = [[-1,-1,-1]]
    x_keys = list(dictionaries_tree.keys())

    if len(x_keys) == 0:
        return default_triples

    xys = list(map(lambda x_key: list(product([x_key], dictionaries_tree[x_key].keys())), x_keys))
    xys_clean = reduce(lambda xy, total: total + xy, xys)
    xyzs = list(
        map(lambda xy_clean: list(product([xy_clean], dictionaries_tree[xy_clean[0]][xy_clean[1]].keys())), xys_clean))
    xyzs_products = reduce(lambda xyz, total: xyz + total, xyzs)
    xyzs_clean = list(
        map(lambda xyzs_product: [xyzs_product[0][0], xyzs_product[0][1], xyzs_product[1]], xyzs_products))
    return xyzs_clean


def get_stats(block_model, units):
    blocks = get_leaf_values_from_dictionaries_tree(block_model)
    total_weight = sum(map(lambda block: get_block_weight(block), blocks))
    blocks_number = len(blocks)
    air_blocks_number = len(filter(lambda block: get_block_weight(block) == 0, blocks))
    total_mineral_weight = sum(map(lambda block: get_block_mineral_weight(block, units), blocks))

    return dict(
        blocks_number=blocks_number,
        total_weight=total_weight,
        total_mineral_weight=total_mineral_weight,
        air_blocks_number=air_blocks_number)


if __name__ == "__main__":
    file_name, coordinates, weight, ores, units = load_file_menu()
    blocks_as_list_of_parameters = load_file(file_name)
    blocks = create_blocks_model(blocks_as_list_of_parameters=blocks_as_list_of_parameters,
                                 coordinates=coordinates,
                                 ores=ores,
                                 weight=weight)

    while True:
        option = int(input('[1] Search for block\n '
                           '[2] Show blocks satistics\n'
                           '\n'
                           'Insert an option: '))
        if option == 1:
            input_to_search = input('Insert x,y,z to search for block info (eg 0,1,0): ')
            x, y, z = [index for index in input_to_search.split(',')]
            block = blocks[x][y][z]
            show_block_info(block, units)

        elif option == 2:

            stats = get_stats(blocks, units)
            print('Statistics: ')
            print('Total blocks\t: ', stats['blocks_number'])
            print('Total weight\t: ', stats['total_weight'])
            print('Mineral weight\t: ', stats['total_mineral_weight'])
            print('Air blocks (%)\t: ', stats['air_blocks_number'])
        break
