from typing import List


class Email:
    def __init__(self, sender: str, receiver: str, content: str) -> None:
        self.sender: str = sender
        self.receiver: str = receiver
        self.content: str = content
        self.is_sent: bool = False

    def send(self) -> None:
        self.is_sent = True

    def get_info(self) -> str:
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


line_in: str = str()
emails: List[Email] = list()

while True:
    line_in = input()
    if line_in == "Stop":
        break
    else:
        emails.append(Email(*line_in.split(' ')))

for i in [ int(ei) for ei in input().split(', ') ]:
    emails[i].send()

for email in emails:
    print(email.get_info())
