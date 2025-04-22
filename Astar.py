class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.heuristic = heuristic
        self.cost = depth + heuristic

def misplaced_tiles(state, goal):
    return sum(state[i][j] != goal[i][j] and state[i][j] != 0 for i in range(3) for j in range(3))

def get_neighbors(state):
    neighbors = []
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                x, y = r, c
    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
    for move, (dx, dy) in moves.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((new_state, move))
    return neighbors

def a_star_search(initial, goal):
    open_list = []
    closed = []
    root = Puzzle(initial, None, "", 0, misplaced_tiles(initial, goal))
    open_list.append(root)
    
    while open_list:
        # Get node with lowest cost (manually)
        current = min(open_list, key=lambda node: node.cost)
        open_list.remove(current)

        if current.state == goal:
            path = []
            while current.parent:
                path.append((current.move, current.state, current.depth, current.heuristic))
                current = current.parent
            return path[::-1], root.depth, root.heuristic, root.cost

        closed.append(current.state)

        for state, move in get_neighbors(current.state):
            if state not in closed:
                g = current.depth + 1
                h = misplaced_tiles(state, goal)
                child = Puzzle(state, current, move, g, h)

                skip = False
                for node in open_list:
                    if node.state == state and node.cost <= child.cost:
                        skip = True
                        break
                if not skip:
                    open_list.append(child)
    return None, 0, 0, 0

def print_solution(path, initial, g, h, f):
    def fmt(row): return " ".join(str(n) if n != 0 else " " for n in row)
    print("\nInitial State:")
    print(f"g(n): {g} | h(n): {h} | f(n): {f}")
    for row in initial:
        print(fmt(row))

    print("\nSolution Steps:")
    for move, state, g, h in path:
        print(f"\nMove: {move} | g(n): {g} | h(n): {h} | f(n): {g+h}")
        for row in state:
            print(fmt(row))
    print("\nGoal Reached!")

def read_state(prompt):
    print(prompt)
    return [list(map(int, input(f"Enter row {i+1} : ").split())) for i in range(3)]

# Driver
if __name__ == "__main__":
    initial = read_state("Enter Initial State:")
    goal = read_state("Enter Goal State:")
    result = a_star_search(initial, goal)
    if result[0]:
        path, g, h, f = result
        print_solution(path, initial, g, h, f)
    else:
        print("No solution found.")
