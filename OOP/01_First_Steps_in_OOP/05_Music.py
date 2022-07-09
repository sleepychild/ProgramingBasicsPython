class Music:
    def __init__(self, title: str, artist: str, lyrics: str) -> None:
        self.title: str = title
        self.artist: str = artist
        self.lyrics: str = lyrics

    def print_info(self) -> str:
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self) -> str:
        return self.lyrics
