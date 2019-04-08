def check_row(dictionary, index):
    if index not in dictionary.keys():
        dictionary[index] = {}
    return


def insert_into_block(blocks, coordinates, weight, minerals):
    check_row(blocks, coordinates['x'])
    check_row(blocks[coordinates['x']], coordinates['y'])
    check_row(blocks[coordinates['x']][coordinates['y']], coordinates['z'])
    blocks[coordinates['x']][coordinates['y']][coordinates['z']] = {
        'weight': weight,
        'minerals': minerals
    }


def load_file(file_name, coordinates, weight, grades):
    blocks = {}
    input_file = open(file_name, 'r')
    for line in input_file:
        split_line = line.split(' ')
        coords = {
            'x': split_line[coordinates['x']],
            'y': split_line[coordinates['y']],
            'z': split_line[coordinates['z']]
        }
        minerals = {}
        for mineral in grades.keys():
            minerals[mineral] = split_line[grades[mineral]]
        line_weight = split_line[weight]
        insert_into_block(blocks, coords, line_weight, minerals)
    input_file.close()

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
        units[grade_name] = input ('Enter the units for the grade (ppm or %):')
    return file_name, coordinates, weight, grades, units


def show_block_info(block,units):
    print('')
    print ('Block info: ')
    print ('Weight\t:',block['weight'])
    if (block['minerals']):

        for mineral in block['minerals'].keys():
            print (mineral,'\t:', block['minerals'][mineral], units[mineral])

def show_stats(blocks,units):
    total_weight = 0
    blocks_number = 0
    air_blocks_number = 0
    total_mineral_weight = 0
    for x_key in blocks.keys():
        for y_key in blocks[x_key].keys():
            for z_key in blocks[x_key][y_key].keys():
                block = blocks[x_key][y_key][z_key]
                block_weight = float(block['weight'])
                if block_weight == 0:
                    air_blocks_number += 1

                total_weight += block_weight
                blocks_number += 1

                for mineral in block['minerals'].keys():
                    mineral_metric = float(block['minerals'][mineral])
                    mineral_unit = units[mineral]
                    if mineral_unit == 'ppm':
                        total_mineral_weight += mineral_metric*block_weight/1000000
                    elif mineral_unit =='%':
                        total_mineral_weight += block_weight*float(mineral_metric)



    print ('Statistics: ')
    print ('Total blocks\t: ',blocks_number)
    print ('Total weight\t: ',total_weight)
    print ('Mineral weight\t: ',total_mineral_weight)
    print ('Air blocks (%)\t: ',air_blocks_number)

if __name__ == "__main__":
    file_name, coordinates, weight, grades, units = load_file_menu()
    blocks = load_file(file_name, coordinates, weight, grades)
    while True:
        option = int(input ('[1] Search for file\n '
                        '[2] Show blocks satistics\n'
                        '\n'
                        'Insert an option: '))
        if option == 1:
            input_to_search = input('Insert x,y,z to search for block info (eg 0,1,0): ')
            x, y, z = [(index) for index in input_to_search.split(',')]
            block = blocks[x][y][z]
            show_block_info(block,units)

        elif option == 2:
            show_stats(blocks,units )

        break

