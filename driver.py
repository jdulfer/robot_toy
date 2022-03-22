from table import Table
import fileinput

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
        print(x,y,f)
        table.place_robot(x,y,f)
    elif instruction[0] == "MOVE":
        table.robots[0].move()
    elif instruction[0] == "RIGHT":
        table.robots[0].right()
    elif instruction[0] == "LEFT":
        table.robots[0].left()
    elif instruction[0] == "REPORT":
        table.report()
        

for line in fileinput.input(files = 'instructions.txt'):
    process(line)
