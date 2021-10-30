class CinemaClass:
    screenings: list = list()
    current_screening: str
    tickets_types: tuple = (
        'student',
        'standard',
        'kid',
    )

    def screen_movie(self, name: str, seats: int) -> None:
        self.current_screening = name
        self.screenings.append({ScreeningClass(name, seats)})

    def sell_ticket(self, ticket_type: str) -> None:
        self.screenings[-1].tickets[self.tickets_types.index(ticket_type)] += 1

    def __str__(self) -> str:
        class_string: str = str()
        ticket_type_index: int
        total_tickets: list = [0] * 3
        for movie, screening in self.screenings.items():
            class_string += f'{movie} - {screening.get_seats_full_percent():.2f}% full.\n'
            for ticket_type in self.tickets_types:
                ticket_type_index = self.tickets_types.index(ticket_type)
                total_tickets[ticket_type_index] += screening.tickets[ticket_type_index]

        class_string += f'Total tickets: {sum(total_tickets)}\n'
        # 66.67% student tickets.
        # 25.00% standard tickets.
        # 8.33% kids tickets.
        return class_string

class ScreeningClass:
    name: str
    seats: int
    tickets: list = [0] * 3

    def __init__(self, name: str, seats: int) -> None:
        self.name = name
        self.seats = seats

    def get_seats_full_percent(self) -> float:
        return sum(self.tickets) / self.seats * 100
    
    def __str__(self) -> str:
        return f'{self.name} - {self.seats} - {self.tickets}'

if __name__ == '__main__':
    cinema: CinemaClass = CinemaClass()
    movie_name: str
    while True:    
        input_data = input()
        if input_data == 'Finish':
            break
        movie_name = input_data
        cinema.screen_movie(movie_name, int(input()))
        while True:
            input_data = input()
            if input_data == 'End':
                break
            cinema.sell_ticket(input_data)

    print(cinema)
