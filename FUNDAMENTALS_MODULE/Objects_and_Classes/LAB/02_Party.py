from typing import List


class Party:
    def __init__(self) -> None:
        self.people: List[str] = list()

    def add_person(self, name: str) -> None:
        self.people.append(name)

    def __str__(self) -> str:
        rtrn_str: str = str()
        rtrn_str += f'Going: {", ".join(self.people)}\n'
        rtrn_str += f'Total: {len(self.people)}'
        return rtrn_str


if __name__ == '__main__':
    cmd_in: str = str()
    prty: Party = Party()

    while True:
        cmd_in = input()
        if cmd_in == "End":
            print(prty)
            exit(0)
        else:
            prty.add_person(cmd_in)
