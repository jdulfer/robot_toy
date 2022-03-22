class Robot:
    def __init__(self, x, y, f):
        # need to validate that the placement location is valid
        self.x = x
        self.y = y
        self.f = f

        # this could probably live on the table rather than the robot but I have it here for simplicity
        self.direction_dict = {
            0: "NORTH",
            1: "EAST",
            2: "SOUTH",
            3: "WEST"
        }

    def move(self):
        # currently this method just opts to ignore invalid move instructions rather than raising an error
        if self.f == 0 and self.x < 3:
            self.x += 1
        elif self.f == 1 and self.y < 3:
            self.y += 1
        elif self.f == 2 and self.x > 0:
            self.x -= 1
        elif self.f == 3 and self.y > 0:
            self.y -= 1
    
    def report(self, number):
        # might need to simplify this report function so it plays nice with any exterior testing
        print(f"Robot number {number}'s location is:", [self.x, self.y, self.direction_dict[self.f]])