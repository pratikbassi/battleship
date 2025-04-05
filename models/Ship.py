class Ship:

    def __init__(self, name: str, coords: tuple, direction: str):
        self.shipData = {
            "Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2
        }
        self.name = name
        self.size = self.shipData[name]
        self.coords = coords
        self.direction = direction
        self.destroyed = False

    def __str__(self):
        return f"Ship: {self.name}, Size: {self.size}, Destroyed: {self.destroyed}"