from List_Manipulation_test_data import input_data, results_data, input_data_cmd

for iteration in range(len(input_data)):

    list_of_numbers = input_data[iteration].split(' ')
    cmd_gen = (c for c in input_data_cmd[iteration])
    print(f'RUN: {iteration} with {list_of_numbers}')

    command = next(cmd_gen)

    new_list = []
    max_even = -1
    max_odd = -1
    min_even = 10000
    min_odd = 10000

    index_max_even = -1
    index_max_odd = -1
    index_min_even = -1
    index_min_odd = -1

    counter = 0
    list_count = []
    invalid_count = 'no'

    while command != 'end':
        split_command = command.split(' ')
        invalid_count = 'no'

        if split_command[0] == 'exchange':
            print(command, end=" => ")
            new_list.clear()
            a = int(len(list_of_numbers))
            index = int(split_command[1])
            if 0 <= index <= a:
                for i in range(index+1, a):
                    new_list.append(list_of_numbers[i])
                for i in range(index+1):
                    new_list.append(list_of_numbers[i])
                list_of_numbers.clear()
                list_of_numbers.extend(new_list)
            if a < index or index < 0:
                print("Invalid index")
            else:
                print(list_of_numbers)

        if split_command[0] == 'max':
            print(command, end=" => ")
            if split_command[1] == 'even':
                for i in range(len(list_of_numbers)):
                    if int(list_of_numbers[i]) % 2 == 0:
                        if max_even <= int(list_of_numbers[i]):
                            max_even = int(list_of_numbers[i])
                            index_max_even = i
                if max_even > -1:
                    print(index_max_even)
                    index_max_even = -1
                    max_even = -1
                else:
                    print('No matches')
                    index_max_even = -1
                    max_even = -1

            if split_command[1] == 'odd':
                for i in range(len(list_of_numbers)):
                    if int(list_of_numbers[i]) % 2 == 1:
                        if max_odd <= int(list_of_numbers[i]):
                            max_odd = int(list_of_numbers[i])
                            index_max_odd = i
                if max_odd > -1:
                    print(index_max_odd)
                    index_max_odd = -1
                    max_odd = -1
                else:
                    print('No matches')
                    index_max_odd = -1
                    max_odd = -1

        if split_command[0] == 'min':
            print(command, end=" => ")
            if split_command[1] == 'even':
                for i in range(len(list_of_numbers)):
                    if int(list_of_numbers[i]) % 2 == 0:
                        if min_even >= int(list_of_numbers[i]):
                            min_even = int(list_of_numbers[i])
                            index_min_even = i
                if min_even < 10000:
                    print(index_min_even)
                    index_min_even = -1
                    min_even = 10000
                else:
                    print('No matches')
                    index_min_even = -1
                    min_even = 10000

            if split_command[1] == 'odd':
                for i in range(len(list_of_numbers)):
                    if int(list_of_numbers[i]) % 2 == 1:
                        if min_odd >= int(list_of_numbers[i]):
                            min_odd = int(list_of_numbers[i])
                            index_min_odd = i
                if min_odd < 10000:
                    print(index_min_odd)
                    index_min_odd = -1
                    min_odd = 1000
                else:
                    print('No matches')
                    index_min_odd = -1
                    min_odd = 1000

        if split_command[0] == 'first':
            print(command, end=" => ")
            if int(split_command[1]) > int(len(list_of_numbers)):
                print('Invalid count')
                invalid_count = 'yes'

            if int(split_command[1]) <= int(len(list_of_numbers)):
                for i in range(len(list_of_numbers)):
                    if split_command[2] == 'even':
                        if int(list_of_numbers[i]) % 2 == 0:
                            counter += 1
                            list_count.append(list_of_numbers[i])
                            if counter == int(split_command[1]):
                                break
                    if split_command[2] == 'odd':
                        if int(list_of_numbers[i]) % 2 == 1:
                            counter += 1
                            list_count.append(list_of_numbers[i])
                            if counter == int(split_command[1]):
                                break
                if invalid_count == 'no':
                    counter = 0
                    print('[', end='')
                    print(', '.join(list_count), end='')
                    print(']')
                    list_count.clear()

        if split_command[0] == 'last':
            print(command, end=" => ")
            if int(split_command[1]) > int(len(list_of_numbers)):
                print('Invalid count')
                invalid_count = 'yes'
            if int(split_command[1]) <= int(len(list_of_numbers)):
                list_of_numbers.reverse()
                for i in range(len(list_of_numbers)):
                    if split_command[2] == 'even':
                        if int(list_of_numbers[i]) % 2 == 0:
                            counter += 1
                            list_count.append(list_of_numbers[i])
                            if counter == int(split_command[1]):
                                break
                    if split_command[2] == 'odd':
                        if int(list_of_numbers[i]) % 2 == 1:
                            counter += 1
                            list_count.append(list_of_numbers[i])
                            if counter == int(split_command[1]):
                                break
            if invalid_count == 'no':
                counter = 0
                list_of_numbers.reverse()
                list_count.reverse()
                print('[', end='')
                print(', '.join(list_count), end='')
                print(']')
                list_count.clear()

        command = next(cmd_gen)
    print("end => ", list_of_numbers)        
    print('[', end='')
    print(', '.join(list_of_numbers), end='')
    print(']')
    print(results_data[iteration])