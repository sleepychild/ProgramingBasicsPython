from typing import Dict, List, Tuple, Generator, Callable, Union

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    # (
    #     '5',
    #     'Red Bazgargal 100 2500 25',
    #     'Black Dargonax 200 3500 18',
    #     'Red Obsidion 220 2200 35',
    #     'Blue Kerizsa 60 2100 20',
    #     'Blue Algordox 65 1800 50',
    # ),
    # (
    #     '4',
    #     'Gold Zzazx null 1000 10',
    #     'Gold Traxx 500 null 0',
    #     'Gold Xaarxx 250 1000 null',
    #     'Gold Ardrax 100 1055 50',
    # ),
    (
        '12',
        'Black Dargonax null null null',
        'Red Bazgargal 100 2500 25',
        'Black Dargonax 200 3500 18',
        'Red Obsidion 220 2200 35',
        'Blue Kerizsa 60 2100 20',
        'Blue Algordox 65 1800 50',
        'Gold Algordox 65 1800 50',
        'Black Algordox 65 1800 50',
        'Gold Zzazx null 1000 10',
        'Gold Traxx 500 null 0',
        'Gold Xaarxx 250 1000 null',
        'Gold Ardrax 100 1055 50',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.def_stats: Dict[str, int] = {
            "damage": 45,
            "health": 250,
            "armor": 10
        }
        self.types: List[str] = list()
        self.dragons: Dict[str, Dict[str, Union[str, int]]] = dict()

    def run(self) -> None:
        for _ in range(int(input())):
            tpe, nme, dmg, hth, arm = input().split()
            tn: str = f"{tpe}_{nme}"
            if tn not in self.dragons:
                if tpe not in self.types:
                    self.types.append(tpe)
                drgn: Dict[str, Union[str, int]] = {
                    "name": nme,
                    "type": tpe
                }
                drgn.update(self.def_stats)
                if dmg != 'null':
                    drgn["damage"] = int(dmg)
                if hth != 'null':
                    drgn["health"] = int(hth)
                if arm != 'null':
                    drgn["armor"] = int(arm)
                self.dragons[tn] = drgn
            else:
                drgn: Dict[str, Union[str, int]] = dict()
                if dmg != 'null':
                    drgn["damage"] = int(dmg)
                else:
                    drgn["damage"] = self.def_stats["damage"]
                if hth != 'null':
                    drgn["health"] = int(hth)
                else:
                    drgn["health"] = self.def_stats["health"]
                if arm != 'null':
                    drgn["armor"] = int(arm)
                else:
                    drgn["armor"] = self.def_stats["armor"]
                self.dragons[tn].update(drgn)

        for t in self.types:
            dt: List[Dict[str, Union[str, int]]] = sorted(
                [v for v in self.dragons.values() if v['type'] == t],
                key=lambda d: d["name"]
            )
            dt_len: int = len(dt)
            ad: float = sum([a["damage"] for a in dt])/dt_len
            ah: float = sum([a["health"] for a in dt])/dt_len
            aa: float = sum([a["armor"] for a in dt])/dt_len
            print(f"{t}::({ad:.2f}/{ah:.2f}/{aa:.2f})")
            for d in dt:
                print(
                    f'-{d["name"]} -> damage: {d["damage"]}, health: {d["health"]}, armor: {d["armor"]}')


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
