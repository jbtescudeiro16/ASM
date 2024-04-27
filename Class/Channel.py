class Channel:
    def __init__(self, x, y, id):
        self.id = f"Channel {id}"
        self.x = x
        self.y = y
        self.available = True
        self.boat = None
        self.state_boat = None

    def get_id(self):
        return self.id

    def get_boat(self):
        return self.boat

    def get_state_boat(self):
        return self.state_boat

    def get_coords(self):
        return self.x, self.y

    def get_available(self):
        return self.available

    def set_available(self, availability):
        self.available = availability

    def set_boat(self, boat, state):
        self.boat = boat
        self.state_boat = state
        self.available=False

    def remove_boat(self):
        self.boat = None
        self.state_boat = None

    def __str__(self):
        return f"##########################################################\n ID: {self.get_id()}, Boat: {self.get_boat()}, State: {self.get_state_boat()}, Coords: {self.get_coords()}, Available: {self.get_available()} \n ##########################################################"
