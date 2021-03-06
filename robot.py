class Robot:
    def __init__(self, x, y, f):
        # validate that the placement location is valid
        if x < 0 or x > 4:
            raise ValueError("x must be between 0 and 4")
        if y < 0 or y > 4:
            #return an error
            raise ValueError("y must be between 0 and 4")
        self.x = x
        self.y = y
        self.f = f

        Robot.direction_dict = {
            0: "NORTH",
            1: "EAST",
            2: "SOUTH",
            3: "WEST"
        }

    def move(self):
        # currently this method just opts to ignore invalid move instructions rather than raising an error
        # could instead have a property decorator on the x y and f values to raise errors properly
        if self.f == 0 and self.y < 4:
            self.y += 1
        elif self.f == 1 and self.x < 4:
            self.x += 1
        elif self.f == 2 and self.y > 0:
            self.y -= 1
        elif self.f == 3 and self.x > 0:
            self.x -= 1

    def left(self):
        if self.f == 0:
            self.f = 3
        else:
            self.f -= 1
    
    def right(self):
        if self.f == 3:
            self.f = 0
        else:
            self.f += 1

    def report(self, number):
        # might need to simplify this report function so it plays nice with any exterior testing
        print(f"Robot number {number}'s location is:", [self.x, self.y, Robot.direction_dict[self.f]])