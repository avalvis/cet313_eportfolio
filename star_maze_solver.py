import math
import numpy as np

# Maze Solver class implementing A* algorithm
class MazeSolver:
    def __init__(self, maze_board):
        # Initialize with the provided maze board
        self.board = maze_board
        self.end_point = (0, 0)  # Goal position

        # Locate the start and end points in the maze
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col].lower() == "o":
                    self.start_point = (col, row)
                elif self.board[row][col].lower() == "x":
                    self.end_point = (col, row)

    def get_possible_actions(self, position):
        # Determine possible moves from the current position
        moves = []
        for move in MOVEMENT_COSTS:
            newX, newY = self.calculate_result(position, move)
            if self.is_position_valid(newX, newY):
                moves.append(move)
        return moves

    def calculate_result(self, position, action):
        # Get new position based on the action
        x, y = position
        if "up" in action:
            y -= 1
        if "down" in action:
            y += 1
        if "left" in action:
            x -= 1
        if "right" in action:
            x += 1
        return (x, y)

    def check_goal(self, position):
        # Verify if the current position is the goal
        return position == self.end_point

    def move_cost(self, position, action, next_position):
        # Return the cost of a specific action
        return MOVEMENT_COSTS[action]

    def estimate_heuristic(self, position):
        # Heuristic estimate using Euclidean distance
        x, y = position
        goal_x, goal_y = self.end_point
        return math.sqrt((x - goal_x) ** 2 + (y - goal_y) ** 2)

    def is_position_valid(self, x, y):
        # Check if the position is valid (inside maze and not a wall)
        return 0 <= x < len(self.board[0]) and 0 <= y < len(self.board) and self.board[y][x] != "#"

    def execute_astar(self):
        # Implement the A* search algorithm
        open_set, closed_set = set(), set()
        start = self.start_point
        open_set.add(start)

        path_history = {}
        g_score = {start: 0}
        f_score = {start: self.estimate_heuristic(start)}

        while open_set:
            current = min(open_set, key=lambda pos: f_score[pos])

            if self.check_goal(current):
                return self.build_path(path_history, current)

            open_set.remove(current)
            closed_set.add(current)

            for move in self.get_possible_actions(current):
                next_pos = self.calculate_result(current, move)
                if next_pos in closed_set:
                    continue

                tentative_g_score = g_score[current] + self.move_cost(current, move, next_pos)

                if next_pos not in open_set or tentative_g_score < g_score[next_pos]:
                    path_history[next_pos] = current
                    g_score[next_pos] = tentative_g_score
                    f_score[next_pos] = tentative_g_score + self.estimate_heuristic(next_pos)

                    if next_pos not in open_set:
                        open_set.add(next_pos)

        return None

    def build_path(self, path_history, current_position):
        # Construct the path from start to goal
        path = [current_position]
        while current_position in path_history:
            current_position = path_history[current_position]
            path.append(current_position)
        return path[::-1]

# Main execution block
if __name__ == "__main__":
    # Define the maze layout
    MAZE_LAYOUT = """
    ##############################
    #         #              #   #
    ######    ########       #   #
    #    #   #               #   #
    #    #####   ###    ######   #
    # o    #   ###   #           #
    #      #     #   #  #  #   ###
    #     #####    #    #  #  x  #
    #              #       #     #
    ##############################
    """
    print(MAZE_LAYOUT)

    # Convert the maze layout to a list
    maze_board = [list(row) for row in MAZE_LAYOUT.split("\n") if row]

    # Movement costs
    MOVEMENT_COSTS = {
        "up": 1.0,
        "down": 1.0,
        "left": 1.0,
        "right": 1.0,
        "up left": 1.4,
        "up right": 1.4,
        "down left": 1.4,
        "down right": 1.4,
    }

    # Initialize the MazeSolver with the maze board
    maze_solver = MazeSolver(maze_board)
    solution = maze_solver.execute_astar()
    print("Solution Path:", solution)