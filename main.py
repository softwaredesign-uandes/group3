def check_row(dictionary, index):
    if index not in dictionary.keys():
        dictionary[index] = {}
    return


def insert_into_blocks(blocks, block, coordinates):
    check_row(blocks, coordinates['x'])
    check_row(blocks[coordinates['x']], coordinates['y'])
    check_row(blocks[coordinates['x']][coordinates['y']], coordinates['z'])
    blocks[coordinates['x']][coordinates['y']][coordinates['z']] = block


def load_file(file_name):
    input_file = open(file_name, 'r')
    blocks_as_list_of_parameters = []
    for line in input_file:
        block_as_list_of_parameters = line.split(' ')
        blocks_as_list_of_parameters.append(block_as_list_of_parameters)
    input_file.close()
    return blocks_as_list_of_parameters


def create_blocks_model(blocks_as_list_of_parameters, coordinates, grades, weight):
    blocks = {}
    for block_as_list_of_parameters in blocks_as_list_of_parameters:
        block_coords = {
            'x': block_as_list_of_parameters[coordinates['x']],
            'y': block_as_list_of_parameters[coordinates['y']],
            'z': block_as_list_of_parameters[coordinates['z']]
        }

        block_minerals = {}
        for mineral in grades.keys():
            block_minerals[mineral] = block_as_list_of_parameters[grades[mineral]]
        block_weight = block_as_list_of_parameters[weight]
        block = dict(minerals=block_minerals, weight=block_weight)
        insert_into_blocks(blocks, block, block_coords)
    return blocks


def load_file_menu():
    file_name = input('Enter the file name: ')
    coordinates = {}
    grades = {}
    coordinates['x'] = int(input('Enter the position of the x coordinate: '))
    coordinates['y'] = int(input('Enter the position of the y coordinate: '))
    coordinates['z'] = int(input('Enter the position of the z coordinate: '))
    weight = int(input('Enter the position of the weight parameter: '))
    number_of_grades = int(input('Enter the quantity of grades for the blocks: '))
    units = {}
    for grade in range(number_of_grades):
        grade_name = input('Enter the name for the grade: ')
        grades[grade_name] = int(input('Enter the coordinate for the grade: '))
        units[grade_name] = input('Enter the units for the grade (ppm or %):')
    return file_name, coordinates, weight, grades, units


def show_block_info(block, units):
    print('')
    print ('Block info: ')
    print ('Weight\t:', block['weight'])
    if (block['minerals']):

        for mineral in block['minerals'].keys():
            print (mineral, '\t:', block['minerals'][mineral], units[mineral])

def get_block_mineral_weight(block, units):
    block_weight = get_block_weight(block)
    mineral_weight = 0
    for mineral in block['minerals'].keys():
        mineral_metric = float(block['minerals'][mineral])
        mineral_unit = units[mineral]
        if mineral_unit == 'ppm':
            mineral_weight += mineral_metric * block_weight / 1000000
        elif mineral_unit == '%':
            mineral_weight += block_weight * (mineral_metric/100.0)
    return mineral_weight

def get_block_weight(block):
    block_weight = float(block['weight'])
    return block_weight

def get_stats(blocks, units):
    total_weight = 0
    blocks_number = 0
    air_blocks_number = 0
    total_mineral_weight = 0
    for x_key in blocks.keys():
        for y_key in blocks[x_key].keys():
            for z_key in blocks[x_key][y_key].keys():
                block = blocks[x_key][y_key][z_key]
                block_weight = get_block_weight(block)

                total_weight += block_weight
                if block_weight == 0:
                    air_blocks_number += 1
                blocks_number += 1

                block_mineral_weight = get_block_mineral_weight(block,units)
                total_mineral_weight += block_mineral_weight
    return dict(
        blocks_number=blocks_number,
        total_weight=total_weight,
        total_mineral_weight=total_mineral_weight,
        air_blocks_number=air_blocks_number)


if __name__ == "__main__":
    file_name, coordinates, weight, grades, units = load_file_menu()
    blocks_as_list_of_parameters = load_file(file_name)
    blocks = create_blocks_model(blocks_as_list_of_parameters=blocks_as_list_of_parameters,
                                 coordinates=coordinates,
                                 grades=grades,
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
            print ('Statistics: ')
            print ('Total blocks\t: ', stats['blocks_number'])
            print ('Total weight\t: ', stats['total_weight'])
            print ('Mineral weight\t: ', stats['total_mineral_weight'])
            print ('Air blocks (%)\t: ', stats['air_blocks_number'])
        break
