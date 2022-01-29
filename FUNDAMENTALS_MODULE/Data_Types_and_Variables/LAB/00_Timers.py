import time

counter: int = int()
tic: float = time.perf_counter()
toc: float = float()

while True:
    time.sleep(.1)
    toc = time.perf_counter()
    if toc - tic > 1:
        counter += 1
        tic = toc
        print(counter)
