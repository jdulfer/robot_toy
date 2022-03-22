from table import Table

table = Table()
table.place_robot(0,0,0)
table.place_robot(1,1,1)
table.place_robot(5,5,1)
table.report()

print("-"*100)

table.robots[0].move()
table.report()

print("-"*100)

table.robots[0].right()
table.robots[0].move()
table.robots[0].move()
table.report()