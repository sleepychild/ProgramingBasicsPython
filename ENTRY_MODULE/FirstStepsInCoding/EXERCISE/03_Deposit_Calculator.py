deposit = float(input())
period = int(input())
rate = float(input()) * 0.01
print(deposit + period * ((deposit * rate) / 12))
