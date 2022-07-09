from typing import List


class SteamUser:
    def __init__(self, username: str, games: List[str]) -> None:
        self.username: str = username
        self.games: List[str] = games
        self.played_hours: int = int()

    def play(self, game: str, hours: int) -> str:
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game: str) -> str:
        if game in self.games:
            return f"{game} is already in your library"
        else:
            self.games.append(game)
            return f"{self.username} bought {game}"

    def status(self) -> str:
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
