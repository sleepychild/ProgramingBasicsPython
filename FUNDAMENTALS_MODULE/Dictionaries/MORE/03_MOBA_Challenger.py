from typing import Dict, List, Tuple, Generator, Callable

DEBUG: bool = False

TEST_RUNS: Tuple[Tuple[str]] = (
    (
        'Peter -> Adc -> 400',
        'George -> Jungle -> 300',
        'Simon -> Mid -> 200',
        'Simon -> Support -> 250',
        'Season end',
    ),
    (
        'Peter -> Adc -> 400',
        'Bush -> Tank -> 150',
        'Frank -> Mid -> 200',
        'Frank -> Support -> 250',
        'Frank -> Tank -> 250',
        'Peter vs Frank',
        'Frank vs Bush',
        'Frank vs Hide',
        'Season end',
    ),
)


def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        return next(test_data_gen)
    return generate_input


class ControlClass:

    def __init__(self) -> None:
        self.players: Dict[str, Dict[str, int]] = dict()

    def run(self) -> None:
        while True:
            lin: str = input()
            if lin == 'Season end':
                break

            if ' -> ' in lin:
                player, position, skill = lin.split(' -> ')
                if player not in self.players:
                    self.players[player] = dict()

                if position not in self.players[player]:
                    self.players[player][position] = int(skill)
                else:
                    self.players[player][position] = max(
                        int(skill), self.players[player][position])

            if ' vs ' in lin:
                player_a, player_b = lin.split(' vs ')
                if player_a in self.players and player_b in self.players:
                    plr_a_pos: List = list(self.players[player_a].keys())
                    plr_b_pos: List = list(self.players[player_b].keys())
                    plr_m_pos: List = [p for p in plr_a_pos if p in plr_b_pos]
                    if plr_m_pos:
                        if sum(self.players[player_a].values()) > sum(self.players[player_b].values()):
                            self.players.pop(player_b)
                        elif sum(self.players[player_a].values()) < sum(self.players[player_b].values()):
                            self.players.pop(player_a)
                        else:
                            pass

        self.players = dict(sorted(self.players.items()))
        self.players = dict(sorted(self.players.items(),
                            key=lambda p: sum(p[1].values()), reverse=True))

        for plrk, plrv in self.players.items():
            plrv = dict(sorted(plrv.items()))
            plrv = dict(sorted(plrv.items(), key=lambda v: v[1], reverse=True))
            self.players[plrk] = plrv

        for plrk, plrv in self.players.items():
            print(f"{plrk}: {sum(plrv.values())} skill")
            for sk, sv in plrv.items():
                print(f"- {sk} <::> {sv}")


def solution():
    ctrl: ControlClass = ControlClass()
    ctrl.run()


if DEBUG:
    for test_run in TEST_RUNS:
        input: Callable[[], str] = get_run_generator(test_run)
        solution()
else:
    solution()
