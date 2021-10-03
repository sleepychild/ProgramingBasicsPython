bird_menu: float = 10.35
fish_menu: float = 12.4
fucking_looser_menu: float = 8.15
desert: float = 1.2
delivery: float = 2.5

total: float = float()
total += bird_menu * int(input())
total += fish_menu * int(input())
total += fucking_looser_menu * int(input())

print(total * desert + delivery)
