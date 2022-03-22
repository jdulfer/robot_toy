from robot import Robot

class Table:
    def __init__(self):
        self.robots = []

    def place_robot(self, x, y, f):
        self.robots.append(Robot(x,y,f))

    def report(self):
        robot_number = 1
        for robot in self.robots:
            robot.report(robot_number)
            robot_number += 1