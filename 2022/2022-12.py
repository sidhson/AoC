import load_data

dl = load_data.DataLoader(day=12)
data = dl.get_data(as_list=True)


import numpy as np
import networkx as nx

height_map = np.array([list(d) for d in data])
print(height_map)

start_index = np.where(height_map == 'S')
start_index = (start_index[0][0], start_index[1][0])
finish_index = np.where(height_map == 'E')
finish_index = (finish_index[0][0], finish_index[1][0])
print(start_index, finish_index)


# Add the starting spots for part 2.
starting_spots = []
for row in range(len(height_map)):
    for col in range(len(height_map[0])):
        if height_map[row, col] == 'a':
            starting_spots.append((row, col))

# Make sure start and finish is reachable
height_map[start_index] = 'a'
height_map[finish_index] = 'z'

# Create the graph
graph = nx.DiGraph()

# Generate the nodes.
for row in range(len(height_map)):
    for col in range(len(height_map[0])):
        graph.add_node((row, col))


def add_relationships(row, col):
    '''Adds node relatioships in all directions.'''
    for dir_row, dir_col in zip([-1,1,0,0],[0,0,-1,1]): 
        
        if row + dir_row < len(height_map) and row + dir_row >= 0 \
            and col + dir_col < len(height_map[0]) and col + dir_col >= 0: # make sure within bounds

            if height_map[row, col] >= chr(ord(height_map[row+dir_row, col+dir_col])-1):
                graph.add_edge((row,col), (row+dir_row,col+dir_col))

# Generate the relationships.
for row in range(len(height_map)):
    for col in range(len(height_map[0])):
        add_relationships(row, col)

print(graph)


# Part 1
print('Computing single shortest path ...')
path = nx.shortest_path(graph, source=start_index, target=finish_index)
print('Length of shorest path from start:',len(path))

# Part 2
shortest_path_len = 10000
for i, start in enumerate(starting_spots):
    if nx.has_path(graph, source=start, target=finish_index):
        path = nx.shortest_path(graph, source=start, target=finish_index)
        if len(path) < shortest_path_len:
            print(f'Shorter path found at {i}. Length: {len(path)}')
            shortest_path_len = len(path)

print(f'Shortest path of all starting points: {shortest_path_len}')
