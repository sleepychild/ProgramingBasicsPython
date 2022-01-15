room_types: tuple = ('Apartment', 'Studio',)
months: tuple = ('May', 'June', 'July', 'August', 'September', 'October',)

prices: tuple = ((
    65.00, 68.70, 77.00, 77.00, 68.70, 65.00,
),(
    50.00, 75.20, 76.00, 76.00, 75.20, 50.00,
),)

discounts: tuple = ((
    (1.00, 1.00, 1.00, 1.00, 1.00, 1.00,),
    (1.00, 1.00, 1.00, 1.00, 1.00, 1.00,),
    (.90, .90, .90, .90, .90, .90,),
),(
    (1.00, 1.00, 1.00, 1.00, 1.00, 1.00,),
    (.95, 1.00, 1.00, 1.00, 1.00, .95,),
    (.7, .8, 1.00, 1.00, .8, .7,),
),)

month: int = months.index(input())
nights: int = int(input())

discount: int = 0 if nights <= 7 else 1 if nights <= 14 else 2

for room in room_types:
    room_index = room_types.index(room)
    price: float = prices[room_index][month] * nights
    price *= discounts[room_index][discount][month]
    print(f'{room}: {price:.2f} lv.')
