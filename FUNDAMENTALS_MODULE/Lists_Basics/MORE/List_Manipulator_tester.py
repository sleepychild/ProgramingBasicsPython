from typing import List, Callable
from List_Manipulation_test_data import input_data, results_data, input_data_cmd
from List_Manipulator import InvalidIndex, InvalidCount, NoMatches, InteractiveList

class InteractiveListTest(InteractiveList):

    def exchange(self, *args) -> None:
        index: int = int(args[0])
        try:
            self._index_check(index)
        except InvalidIndex as e:
            print(e)
        else:
            for _ in range(index+1):
                self.append(self.pop(0))
            print(self)

    def end(self) -> None:
        print(self)
        # exit(0)

for i in range(len(input_data)):
    interlist: InteractiveListTest = InteractiveListTest.list_from_string(input_data[i], ' ', int)
    print(f'RUN: {i} with {interlist}')
    for command in input_data_cmd[i]:
        command_parts: List[str] = command.split(' ')
        print(command_parts, end=" => ")
        interlist.__getattribute__(command_parts[0])(*command_parts[1:])
    print(interlist)
    print(results_data[i])
