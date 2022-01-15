room_types: tuple = ('room for one person', 'apartment', 'president apartment',)
room_price: tuple = (18.00, 25.00, 35.00,)

feedback: tuple = ('positive', 'negative',)
feedback_mod: tuple = (1.25, .9,)

discount: tuple = (
    (1.00, 1.00, 1.00),
    (.7, .65, .50),
    (.9, .85, .80),
)

days: int = int(input()) - 1
room_type: int = room_types.index(input())
score: int = feedback.index(input())

discount_rate = 0 if days < 10 else 1 if 10 <= days <= 15 else 2
total: float = days * room_price[room_type]
total *= discount[room_type][discount_rate]
total *= feedback_mod[score]

print(f'{total:.2f}')
