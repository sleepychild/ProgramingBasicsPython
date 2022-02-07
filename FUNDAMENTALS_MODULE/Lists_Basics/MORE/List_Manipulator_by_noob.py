from List_Manipulation_test_data import input_data, results_data, input_data_cmd


for iteration in range(len(input_data)):

    initial_list = list(map(int, input_data[iteration].split(' ')))
    cmd_gen = (c for c in input_data_cmd[iteration])
    print(f'RUN: {iteration} with {initial_list}')

    command = next(cmd_gen)

    while command != 'end':
        command = command.split(' ')
        print(command, end=" => ")
        if command[0] == 'exchange':
            index = int(command[1])
            if index >= len(initial_list) or index < 0:
                print('Invalid index')
                command = next(cmd_gen)
                continue
            current_list = []
            for i in range(index+1, (len(initial_list))):
                current_list.append(initial_list[i])
            for i in range(0, index+1):
                current_list.append(initial_list[i])
            initial_list = current_list
            print(initial_list)

        elif command[0] == 'max':
            if command[1] == 'even':
                current_list = []
                for i in initial_list:
                    if i % 2 == 0:
                        current_list.append(i)
                if not current_list:
                    print('No matches')
                else:
                    max_even = max(current_list)
                    for i in range(len(initial_list)-1, -1, -1):
                        if initial_list[i] == max_even:
                            print(i)
                            break
            elif command[1] == 'odd':
                current_list = []
                for i in initial_list:
                    if i % 2 != 0:
                        current_list.append(i)
                if not current_list:
                    print('No matches')
                else:
                    max_odd = max(current_list)
                    for i in range(len(initial_list)-1, -1, -1):
                        if initial_list[i] == max_odd:
                            print(i)
                            break

        elif command[0] == 'min':
            if command[1] == 'even':
                current_list = []
                for i in initial_list:
                    if i % 2 == 0:
                        current_list.append(i)
                if not current_list:
                    print('No matches')
                else:
                    min_even = min(current_list)
                    for i in range(len(initial_list)-1, -1, -1):
                        if initial_list[i] == min_even:
                            print(i)
                            break
            elif command[1] == 'odd':
                current_list = []
                for i in initial_list:
                    if i % 2 != 0:
                        current_list.append(i)
                if not current_list:
                    print('No matches')
                else:
                    min_odd = min(current_list)
                    for i in range(len(initial_list)-1, -1, -1):
                        if initial_list[i] == min_odd:
                            print(i)
                            break

        elif command[0] == 'first':
            count = int(command[1])
            if count > len(initial_list):
                print('Invalid count')
            else:
                if command[2] == 'even':
                    first_even = []
                    for even in initial_list:
                        if even % 2 == 0:
                            first_even.append(even)
                            if len(first_even) == count:
                                break
                    print(first_even)
                elif command[2] == 'odd':
                    first_odd = []
                    for odd in initial_list:
                        if odd % 2 != 0:
                            first_odd.append(odd)
                            if len(first_odd) == count:
                                break
                    print(first_odd)

        elif command[0] == 'last':
            count = int(command[1])
            if count > len(initial_list):
                print('Invalid count')
            else:
                if command[2] == 'even':
                    last_even = []
                    for even in reversed(initial_list):
                        if even % 2 == 0:
                            last_even.append(even)
                            if len(last_even) == count:
                                break
                    last_even.reverse()
                    print(last_even)
                elif command[2] == 'odd':
                    last_odd = []
                    for odd in reversed(initial_list):
                        if odd % 2 != 0:
                            last_odd.append(odd)
                            if len(last_odd) == count:
                                break
                    last_odd.reverse()
                    print(last_odd)
        command = next(cmd_gen)
    print("end")
    print(initial_list)
    print(results_data[iteration])
