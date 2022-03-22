import unittest
from driver import Driver
from unittest.mock import patch
from io import StringIO
import fileinput

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    @patch('sys.stdout', new_callable = StringIO)
    def test_robot_placement(self, stdout):
        self.driver.process("PLACE 0,0,NORTH")
        self.driver.process("REPORT")

        expected_out = "There is 1 robot active\nCurrent active robot is 1\nRobot number 1's location is: [0, 0, 'NORTH']\n"
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable = StringIO)
    def test_robot_movement(self, stdout):
        self.driver.process("PLACE 0,0,NORTH")
        self.driver.process("MOVE")
        self.driver.process("MOVE")
        self.driver.process("RIGHT")
        self.driver.process("MOVE")
        self.driver.process("REPORT")

        expected_out = "There is 1 robot active\nCurrent active robot is 1\nRobot number 1's location is: [1, 2, 'EAST']\n"
        self.assertEqual(stdout.getvalue(), expected_out)

    @patch('sys.stdout', new_callable = StringIO)
    def test_robot_invalid_commands(self, stdout):
        # this should test that invalid commands for the robot don't move the robot or break the driver program
        # it should also test dirving multiple robots at once

        for line in fileinput.input(files = "test_instructions.txt"):
            self.driver.process(line)

        with open('expected_output.txt', 'r') as file:
            expected_out = file.read()
        self.assertEqual(stdout.getvalue(), expected_out)

if __name__ == "__main__":
    unittest.main()