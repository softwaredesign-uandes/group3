def check_row(dictionary, index):
    if index not in dictionary.keys():
        dictionary[index] = {}
    return


def insert_into_block(blocks, coordinates, weight, ores):
    check_row(blocks, coordinates['x'])
    check_row(blocks[coordinates['x']], coordinates['y'])
    check_row(blocks[coordinates['x']][coordinates['y']], coordinates['z'])
    blocks[coordinates['x']][coordinates['y']][coordinates['z']] = {
        'weight': weight,
        'ores': ores
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
        ores = {}
        for ore in grades.keys():
            ores[ore] = split_line[grades[ore]]
        line_weight = split_line[weight]
        insert_into_block(blocks, coords, line_weight, ores)
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
    for grade in range(number_of_grades):
        grade_name = input('Enter the name for the grade: ')
        grades[grade_name] = int(input('Enter the coordinate for the grade: '))
    return file_name, coordinates, weight, grades


if __name__ == "__main__":
    file_name, coordinates, weight, grades = load_file_menu()
    blocks = load_file(file_name, coordinates, weight, grades)
