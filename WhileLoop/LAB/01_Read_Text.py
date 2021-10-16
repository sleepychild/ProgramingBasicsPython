class EchoClass():
    message: str = str()

    def cicle(self) -> bool:
        in_message: str = input()
        in_message = in_message.strip()
        if in_message == 'Stop':
            return False
        else:
            self.message = in_message
            return True

    def run(self):
        while self.cicle():
            print(self.message)

if __name__ == '__main__':
    echoer = EchoClass()
    echoer.run()
