import os
import numpy as np
import heapq

class CaveFinder():
    def __init__(self, cave : np.array) -> None:
        self.dim = cave.shape[0]
        self.no_v = self.dim**2
        self.visited = []
        self.edges = {}
        self.create_edge_list(cave)
        
    def create_edge_list(self, cave : np.array):
        for row in range(self.dim):
            for col in range(self.dim):
                node = row * self.dim + col
                neighbors = []
                if col != 0: neighbors.append((col-1 + row*self.dim, cave[row, col-1]))
                if row != 0: neighbors.append((col + (row-1)*self.dim, cave[row-1, col]))
                if col != self.dim-1: neighbors.append((col+1 + row*self.dim, cave[row, col+1]))
                if row != self.dim-1: neighbors.append((col + (row+1)*self.dim, cave[row+1, col]))
                self.edges[node] = neighbors
    
    def dijkstra(self):
         # All nodes numbered from 0 to 'no_v'
        distances = {v:float('inf') for v in range(self.no_v)}
        distances[0] = 0

        # A heap priority queue is used to go through the path of least cost first.
        q = []
        heapq.heappush(q, (0,0))

        while len(q) != 0:
            _, current_v = heapq.heappop(q)
            self.visited.append(current_v)
            
            for neighbor, neighbor_dist in self.edges[current_v]: # List of tuples with (node_nbr, dist).
                if neighbor not in self.visited:
                    old_cost = distances[neighbor]
                    new_cost = distances[current_v] + neighbor_dist
                    if new_cost < old_cost:
                        heapq.heappush(q, (new_cost, neighbor))
                        distances[neighbor] = new_cost
        return distances


def create_big_cave(small_cave : np.array) -> np.array:
    for row in range(5): 
        single_block = small_cave.copy()
        for _ in range(row):
            single_block = increase_risk_block(single_block)
        row_block = single_block.copy()
        for _ in range(4):
            single_block = increase_risk_block(single_block)
            row_block = np.concatenate((row_block, single_block), axis=1)
        
        if row == 0:
            big_cave = row_block.copy()
        else:
            big_cave = np.concatenate((big_cave, row_block), axis=0)
    return big_cave

def increase_risk_block(block : np.array) -> np.array:
    new_block = block.copy()
    dim = block.shape[0]
    for row in range(dim):
        for col in range(dim):
            if new_block[row, col] == 9:
                new_block[row, col] = 1
            else:
                new_block[row, col] += 1
    return new_block

def main():
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = []
        for line in f.readlines():
            input.append([int(l) for l in line.strip()])
        cave = np.array([l for l in input]).reshape(len(input), len(input[0]))

        # Number all nodes 0, 1, 2, ...
        # Store dict of links between nodes: {start : (end, cost)}
        small_cave = cave
        big_cave = create_big_cave(cave)

        # Larger cave takes a while to run. Should change implementation.
        cf = CaveFinder(big_cave)
        dist = cf.dijkstra()
        
        # print('Ans A test:',dist[99])
        # print('Ans A full:',dist[9999])

        # print('Ans B test:',dist[2499])
        print('Ans B full:',dist[249999]) 
        

if __name__ == '__main__':
    main()