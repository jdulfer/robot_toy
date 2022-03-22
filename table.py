from multiprocessing.sharedctypes import Value
from robot import Robot

class Table:
    def __init__(self):
        self.robots = []

    def place_robot(self, x, y, f):
        try:
            self.robots.append(Robot(x,y,f))
        except ValueError as e:
            # might need to get rid of the value messages in favour of ignoring them
            # print("Invalid placement value")
            # print(e)
            pass

    def report(self):
        robot_number = 1
        for robot in self.robots:
            robot.report(robot_number)
            robot_number += 1