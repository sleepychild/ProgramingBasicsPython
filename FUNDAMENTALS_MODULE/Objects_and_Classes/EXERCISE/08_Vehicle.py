from typing import Union


class Vehicle:
    def __init__(self, type: str, model: str, price: int) -> None:
        self.type: str = type
        self.model: str = model
        self.price: int = price
        self.owner: Union[str, None] = None
    
    def buy(self, money: int, owner: str) -> str:
        if self.owner == None and self.price <= money:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {money - self.price:.2f}'
        elif self.owner != None:
            return 'Car already sold'
        elif self.price > money:
            return 'Sorry, not enough money'
    
    def sell(self) -> Union[str, None]:
        if self.owner == None:
            return 'Vehicle has no owner'
        else:
            self.owner = None
    
    def __repr__(self) -> str:
        if self.owner == None:
            return f'{self.model} {self.type} is on sale: {self.price}'
        else:
            return f'{self.model} {self.type} is owned by: {self.owner}'

# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type,
# model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
