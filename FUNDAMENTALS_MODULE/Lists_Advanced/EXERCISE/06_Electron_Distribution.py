from typing import List

shells: List[int] = list()
shell: int = 1
electrons: int = int(input())

while electrons > 0:
    shell_size: int = 2 * shell ** 2
    if electrons >= shell_size:
        shells.append(shell_size)
        electrons -= shell_size
        shell += 1
    elif electrons > 0:
        shells.append(electrons)
        electrons = 0

print(shells)
