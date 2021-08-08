"""
489. Robot Room Cleaner
Mar 2, 2019 | leetcode |  Hits
Problem description:
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:

room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3
Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot’s position internally. You must solve this problem “blindfolded”. In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot’s position.
The robot’s initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
"""


class Robot:
    def move(self) -> bool:
        pass

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def clean(self):
        pass


class Solution:
    def clean_room(robot: Robot, row: int, col: int):
        def dfs(robot, row, col, cur_dir, visit):
            visit.add((row, col))
            robot.clean()
            for _ in range(4):
                x, y = change_position(row, col, cur_dir)

                if (x, y) in visit:
                    robot.turnRight()
                    cur_dir = (cur_dir + 1) % 4
                    continue

                if robot.move():
                    dfs(robot, x, y, cur_dir, visit)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                else:
                    visit.add((x, y))

                robot.turnRight()
                cur_dir = (cur_dir + 1) % 4

        def change_position(x, y, dir):
            if dir == 0:
                return x, y + 1

            if dir == 1:
                return x + 1, y

            if dir == 2:
                return x, y - 1

            if dir == 3:
                return x - 1, y

        visit = set()

        # 0: up, 1: right, 2: down, 3: down
        cur_dir = 0
        dfs(robot, row, col, cur_dir, visit)
        return




