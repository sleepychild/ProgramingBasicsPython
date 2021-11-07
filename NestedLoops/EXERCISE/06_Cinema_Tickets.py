class CinemaClass:
    screenings: list = list()
    current_screening: str
    tickets_types: tuple = (
        'student',
        'standard',
        'kid',
    )

    def show_screenings(self) -> None:
            print(self.screenings[-1])

    def screen_movie(self, name: str, seats: int) -> None:
        self.current_screening = name
        self.screenings.append(ScreeningClass(name, seats))

    def sell_ticket(self, ticket_type: str) -> bool:
        return self.screenings[-1].sell_ticket(self.tickets_types.index(ticket_type))

    def __str__(self) -> str:
        class_string: str = str()
        ticket_type_index: int
        total_tickets: list = [0] * 3
        for screening in self.screenings:
            for ticket_type in self.tickets_types:
                ticket_type_index = self.tickets_types.index(ticket_type)
                total_tickets[ticket_type_index] += screening.tickets[ticket_type_index]

        total_tickets_sum: int = sum(total_tickets)
        class_string += f'Total tickets: {total_tickets_sum}\n'
        class_string += f'{ total_tickets[0] / total_tickets_sum * 100 :.2f}% student tickets.\n'
        class_string += f'{ total_tickets[1] / total_tickets_sum * 100 :.2f}% standard tickets.\n'
        class_string += f'{ total_tickets[2] / total_tickets_sum * 100 :.2f}% kids tickets.'
        return class_string

class ScreeningClass:
    name: str
    seats: int
    tickets: list

    def __init__(self, name: str, seats: int) -> None:
        self.name = name
        self.seats = seats
        self.tickets = [0] * 3

    def sell_ticket(self, ticket_type_index: int) -> bool:
        self.tickets[ticket_type_index] += 1
        return sum(self.tickets) == self.seats

    def get_seats_full_percent(self) -> float:
        return sum(self.tickets) / self.seats * 100
    
    def __str__(self) -> str:
        return f'{self.name} - {self.get_seats_full_percent():.2f}% full.'

if __name__ == '__main__':
    cinema: CinemaClass = CinemaClass()
    movie_name: str
    while True:    
        input_data = input()
        if input_data == 'Finish':
            print(cinema)
            exit(0)
        movie_name = input_data
        cinema.screen_movie(movie_name, int(input()))
        while True:
            input_data = input()
            if input_data == 'End':
                cinema.show_screenings()
                break
            elif input_data == 'Finish':
                cinema.show_screenings()
                print(cinema)
                exit(0)
            else:
                if cinema.sell_ticket(input_data):
                    cinema.show_screenings()
                    break
