from typing import ClassVar, List

class DayEvent:
    def __init__(self, event_type: str, event_subj: str, event_val: int) -> None:
        self.event_type: str = event_type
        self.event_subj: str = event_subj
        self.event_val: int = event_val


class DayEvents:
    def __init__(self, data_in: str) -> None:
        self.events: List[DayEvent] = list()
        for d_ev in data_in.split('|'):
            d_ev_s, d_ev_v = d_ev.split('-')
            if d_ev_s in ('rest', 'order',):
                self.events.append(DayEvent(d_ev_s, '', int(d_ev_v)))
            else:
                self.events.append(DayEvent('stock_up', d_ev_s, int(d_ev_v)))


class BakerGuy:
    _MAX_ENERGY: ClassVar[int] = 100

    def __init__(self) -> None:
        self.energy: int = 100
        self.coin: int = 100

    def handle_event(self, day_event: DayEvent) -> None:
        self.__getattribute__(day_event.event_type)(day_event)

    def rest(self, d_ev: DayEvent) -> None:
        energy_gain: int = d_ev.event_val
        pre_gain_energy: int = self.energy
        self.energy = min(self.energy + energy_gain, self._MAX_ENERGY)
        print(f'You gained {self.energy - pre_gain_energy} energy.\nCurrent energy: {self.energy}.')
    
    def order(self, d_ev: DayEvent) -> None:
        coin_gain: int = d_ev.event_val
        if self.energy < 30:
            self.energy += 50
            print('You had to rest!')
        else:
            self.energy -= 30
            self.coin += coin_gain
            print(f'You earned {coin_gain} coins.')
    
    def stock_up(self, d_ev: DayEvent) -> None:
        ingredient_name: str = d_ev.event_subj 
        ingredient_cost: int = d_ev.event_val
        if self.coin < ingredient_cost:
            print(f'Closed! Cannot afford {ingredient_name}.')
            exit(0)
        else:
            self.coin -= ingredient_cost
            print(f'You bought {ingredient_name}.')

    def __str__(self) -> str:
        return f'Day completed!\nCoins: {self.coin}\nEnergy: {self.energy}'


if __name__ == '__main__':

    # 8 and 9 are the gotchas.

    # day_events: DayEvents = DayEvents('rest-2|order-10|eggs-100|rest-10')
    # day_events: DayEvents = DayEvents('order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000')
    day_events: DayEvents = DayEvents(input())

    baker_guy: BakerGuy = BakerGuy()

    for day_event in day_events.events:
        baker_guy.handle_event(day_event)

    print(baker_guy)
