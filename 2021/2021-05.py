import os
import numpy as np

def addVents(ocean_floor, start_end, diag=False):
    for X, Y in start_end:
        if X[0] == X[1]: # Horizontal
            for y in range(min(Y),max(Y)+1):
                ocean_floor[y][X[0]] += 1

        elif Y[0] == Y[1]: # Vertical
            for x in range(min(X),max(X)+1):
                ocean_floor[Y[0]][x] += 1

        elif diag:
            dist = max(X) - min(X)
            if X[1] - X[0] == Y[1] - Y[0]: # Trace.
                for i in range(dist + 1):
                    ocean_floor[min(Y) + i][min(X) + i] += 1
            else:
                for i in range(dist + 1):
                    ocean_floor[max(Y) - i][min(X) + i] += 1

    return ocean_floor


def countDangerZones(ocean_floor):
    count = 0
    for zone in ocean_floor.flatten():
        if zone >= 2:
            count += 1
    return count


if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        start_end = []

        for line in f:
            start, end = line.strip().split(' -> ')
            start = start.split(',')
            end = end.split(',')
            X = int(start[0]), int(end[0])
            Y = int(start[1]), int(end[1])
            start_end.append((X,Y))
    
    # Examine largest and smallest values. 
    # xs, ys = zip(*start_end)
    # print('Max:',list(map(max, zip(*xs))), list(map(max, zip(*ys))))
    # print('Min:',list(map(min, zip(*xs))), list(map(min, zip(*ys))))

    n = 1000
    ocean_floor = np.array([0 for _ in range(n*n)]).reshape(n,n)

    ocean_floor_vh = addVents(ocean_floor.copy(), start_end)
    print('Ans A: ', countDangerZones(ocean_floor_vh))

    ocean_floor_diag = addVents(ocean_floor, start_end, diag=True)
    print('Ans B ', countDangerZones(ocean_floor_diag))            
        