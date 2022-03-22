from table import Table
import fileinput
import sys

class Driver:
    def __init__(self):
        self.table = Table()
        Driver.direction_dict = {
        "NORTH": 0,
        "EAST": 1,
        "SOUTH": 2,
        "WEST": 3
        }

    def process(self, line):
        instruction = line.split()
        if instruction[0] == "PLACE":
            coordinates = instruction[1].split(",")
            x = int(coordinates[0])
            y = int(coordinates[1])
            f = Driver.direction_dict[coordinates[2]]
            self.table.place_robot(x,y,f)
        elif instruction[0] == "MOVE":
            self.table.robots[self.table.active_robot].move()
        elif instruction[0] == "RIGHT":
            self.table.robots[self.table.active_robot].right()
        elif instruction[0] == "LEFT":
            self.table.robots[self.table.active_robot].left()
        elif instruction[0] == "REPORT":
            self.table.report()
        elif instruction[0] == "ROBOT":
            # ideally this should be set through the table class with a setter as opposed to directly changed by the driver
            self.table.active_robot = int(instruction[1]) - 1
        else:
            raise ValueError("Invalid instruction")

if __name__ == "__main__":
    driver = Driver()
    if len(sys.argv) == 1:
        for line in fileinput.input():
            driver.process(line)
    else:
        for line in fileinput.input(files = sys.argv[1]):
            driver.process(line)
