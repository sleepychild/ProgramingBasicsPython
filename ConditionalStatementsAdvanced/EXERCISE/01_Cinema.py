ticket_tier: tuple = ('Premiere', 'Normal', 'Discount')
ticket_tier_price: tuple = (12,7.5,5,)
tier: int = ticket_tier.index(input())
print(f'{int(input()) * int(input()) * ticket_tier_price[tier]:.2f} leva')
