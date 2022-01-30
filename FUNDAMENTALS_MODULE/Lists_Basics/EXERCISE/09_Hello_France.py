from typing import List, Generator
from enum import Enum

TICKET_PRICE: int = 150
SELL_MARKUP: float = .4

class MaxPrice(Enum):
    Clothes = 50.00
    Shoes = 35.00
    Accessories = 20.50

class StoreItem:
    def __init__(self,type_in: str, price_in: str) -> None:
        self.item_type: str = type_in
        self.item_price: float = float(price_in)

class Store:
    def __init__(self, data_in: str) -> None:
        self.store_items: List[StoreItem] = list()
        for item_in in data_in.split('|'):
            self.store_items.append(StoreItem(*item_in.split('->')))
    
class Buyer:
    def __init__(self, store_items: List[StoreItem], money_in: str) -> None:
        self.money: float = float(money_in)
        self.items: List[float] = list()
        for store_item in store_items:
            self.buy_item(store_item)
        print(self)

    def buy_item(self, item: StoreItem) -> None:
        if MaxPrice[item.item_type].value >= item.item_price and self.money >= item.item_price:
            self.money -= item.item_price
            self.items.append(item.item_price)

    def __str__(self) -> str:
        string_data: str = str()
        items_list: List[str] = list()
        for item in self.items:
            items_list.append(f'{item+item*SELL_MARKUP :.2f}')
        string_data += ' '.join(items_list)
        string_data += f'\nProfit: {sum(self.items)*SELL_MARKUP:.2f}\n'
        string_data += 'Hello, France!' if (self.money + sum(self.items)*(SELL_MARKUP+1)) >= TICKET_PRICE else 'Not enough money.'
        return string_data
        

Buyer(Store('Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60').store_items, '120')
Buyer(Store('Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60').store_items, '90')
# Buyer(Store(input()).store_items, input())
