from astar_python import Astar

def new_neighbors(self, matrix, current):
    neighbours_list = []
    if current.x - 1 >= 0 and matrix[current.y][current.x - 1].weight is not None:
        neighbours_list.append(matrix[current.y][current.x - 1])
    if current.y - 1 >= 0 and matrix[current.y - 1][current.x].weight is not None:
        neighbours_list.append(matrix[current.y - 1][current.x])
    if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x].weight is not None:
        neighbours_list.append(matrix[current.y + 1][current.x])
    if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1].weight is not None:
        neighbours_list.append(matrix[current.y][current.x + 1])
    return neighbours_list

Astar.neighbours = new_neighbors