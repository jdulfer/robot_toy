from multiprocessing.sharedctypes import Value
from robot import Robot

class Table:
    def __init__(self):
        self.robots = []
        self.active_robot = 0

    def place_robot(self, x, y, f):
        try:
            self.robots.append(Robot(x,y,f))
            self.active_robot = len(self.robots) - 1
        except ValueError as e:
            # I'm not displaying the ValueError messages in favour of ignoring them
            # but I have the code I was using during testing commented below
            
            # print("Invalid placement value")
            # print(e)
            pass

    def report(self):
        if len(self.robots) == 1:
            print(f"There is 1 robot active")
        else:
            print(f"There are {len(self.robots)} robots active")
        print(f"Current active robot is {self.active_robot + 1}")
        robot_number = 1
        for robot in self.robots:
            robot.report(robot_number)
            robot_number += 1