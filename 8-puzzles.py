class EightPuzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        row, col = divmod(zero_index, 3)

        # Possible moves (up, down, left, right)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(state)
                # Swap the zero with the adjacent tile
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))

        return neighbors

    def heuristic(self, state):
        # Using Manhattan distance as the heuristic
        distance = 0
        for i in range(1, 9):
            current_index = state.index(i)
            goal_index = self.goal_state.index(i)
            current_row, current_col = divmod(current_index, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def hill_climbing(self):
        current_state = tuple(self.initial_state)
        while True:
            neighbors = self.get_neighbors(current_state)
            next_state = None
            min_heuristic = self.heuristic(current_state)

            for neighbor in neighbors:
                current_heuristic = self.heuristic(neighbor)
                if current_heuristic < min_heuristic:
                    min_heuristic = current_heuristic
                    next_state = neighbor

            if next_state is None:
                # No better neighbor found, we are at a local maximum
                print("No better neighbors found. Stopping.")
                return current_state

            current_state = next_state

            if current_state == tuple(self.goal_state):
                print("Goal state reached!")
                return current_state


def main():
    # Example usage
    initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Example initial state
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Goal state

    puzzle = EightPuzzle(initial_state, goal_state)
    result = puzzle.hill_climbing()

    print("Final state:", result)


if __name__ == "__main__":
    main()
