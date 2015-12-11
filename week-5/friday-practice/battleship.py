class Field:
    def __init__(self, position, shot_status=False, ship_status=False):
        self.position = position
        self.shot_status = shot_status
        self.ship_status = ship_status


class Ship:
    def __init__(self, size, position):
        self.size = size
        self.position = position
