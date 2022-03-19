from typing import ClassVar


class Movie:
    __watched_movies: ClassVar[int] = int()

    def __init__(self, name: str, director: str) -> None:
        self.name: str = name
        self.director: str = director
        self.watched: bool = False
    
    def change_name(self, new_name: str) -> None:
        self.name = new_name
    
    def change_director(self, new_director: str) -> None:
        self.director = new_director
    
    def watch(self) -> None:
        if not self.watched:
            self.watched = True
            self.__class__.__watched_movies += 1
    
    def __repr__(self) -> str:
        return f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {self.__watched_movies}'

# first_movie = Movie("Inception", "Christopher Nolan")
# second_movie = Movie("The Matrix", "The Wachowskis")
# third_movie = Movie("The Predator", "Shane Black")
# first_movie.change_director("Me")
# third_movie.change_name("My Movie")
# first_movie.watch()
# third_movie.watch()
# first_movie.watch()

# print(first_movie)
# print(second_movie)

# second_movie.watch()

# print(third_movie)
