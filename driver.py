from table import Table
import fileinput
import sys

table = Table()

direction_dict = {
    "NORTH": 0,
    "EAST": 1,
    "SOUTH": 2,
    "WEST": 3
}

def process(line):
    instruction = line.split()
    if instruction[0] == "PLACE":
        coordinates = instruction[1].split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])
        f = direction_dict[coordinates[2]]
        table.place_robot(x,y,f)
    elif instruction[0] == "MOVE":
        table.robots[table.active_robot].move()
    elif instruction[0] == "RIGHT":
        table.robots[table.active_robot].right()
    elif instruction[0] == "LEFT":
        table.robots[table.active_robot].left()
    elif instruction[0] == "REPORT":
        table.report()
    elif instruction[0] == "ROBOT":
        # ideally this should be set through the table class as opposed to directly changed by the driver
        table.active_robot = int(instruction[1]) - 1
        
if len(sys.argv) == 1:
    for line in fileinput.input():
        process(line)
else:
    for line in fileinput.input(files = sys.argv[1]):
        process(line)
