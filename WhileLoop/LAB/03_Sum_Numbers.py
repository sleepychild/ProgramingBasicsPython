class Accumulator:
    target: int
    accumulated: int = 0

    def __init__(self, target_in: int) -> None:
        self.target = target_in

    def ramp_up(self, delta) -> None:
        self.accumulated += delta

    def run(self) -> int:
        while self.target > self.accumulated:
            self.ramp_up(int(input()))
        return self.accumulated

if __name__ == '__main__':
    accum = Accumulator(int(input()))
    print(accum.run())
