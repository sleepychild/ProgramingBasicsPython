elements_count: int = int(input())

histogram: list = [0,0,0,0,0]

for i in range(elements_count):
    element_in: int = int(input())
    if element_in < 200:
        histogram[0]+=1
    elif element_in < 400:
        histogram[1]+=1
    elif element_in < 600:
        histogram[2]+=1
    elif element_in < 800:
        histogram[3]+=1
    else:
        histogram[4]+=1

for d in histogram:
    print(f'{d/elements_count*100:.2f}%')
