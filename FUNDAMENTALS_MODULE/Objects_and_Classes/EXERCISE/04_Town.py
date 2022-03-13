class Town:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.latitude: str = '0°N'
        self.longitude: str = '0°E'

    def set_latitude(self, latitude: str) -> None:
        self.latitude = latitude

    def set_longitude(self, longitude: str) -> None:
        self.longitude = longitude

    def __repr__(self) -> str:
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'

