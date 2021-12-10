import os
import numpy as np

def findLowPoints(heightmap : np.array, get_location = False):
    low_points = []
    
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            
            left_wall = (i == 0)
            up_wall = (j == 0)
            right_wall = (i == len(heightmap)-1)
            down_wall = (j == len(heightmap[0])-1)
            
            current_point = heightmap[i][j]
            low = True
            if not left_wall and heightmap[i-1][j] <= current_point:
                low = False
            elif not up_wall and heightmap[i][j-1] <= current_point:
                low = False
            elif not right_wall and heightmap[i+1][j] <= current_point:
                low = False
            elif not down_wall and heightmap[i][j+1] <= current_point:
                low = False

            if low:
                if get_location:
                    low_points.append((i,j))
                else:
                    low_points.append(current_point)
    return low_points


def findBasinSizes(heightmap : np.array, low_points : list):
    basin_sizes = []

    for point in low_points:
        current_basin = set([point])
        points_to_check = set([point])

        while len(points_to_check) > 0:
            i, j = points_to_check.pop()
            current_basin.add((i,j))

            left_wall = (i == 0)
            up_wall = (j == 0)
            right_wall = (i == len(heightmap)-1)
            down_wall = (j == len(heightmap[0])-1)
            
            if not left_wall and heightmap[i-1][j] != 9 and (i-1,j) not in current_basin:
                points_to_check.add((i-1,j))
            
            if not up_wall and heightmap[i][j-1] != 9 and (i,j-1) not in current_basin:
                points_to_check.add((i,j-1))
            
            if not right_wall and heightmap[i+1][j] != 9 and (i+1,j) not in current_basin:
                points_to_check.add((i+1,j))
            
            if not down_wall and heightmap[i][j+1] != 9 and (i,j+1) not in current_basin:
                points_to_check.add((i,j+1))
        
        basin_sizes.append(len(current_basin))

    return basin_sizes


if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:

        heightmap = []
        for line in f.readlines():
            line = line.strip().split()[0]
            heightmap.append([int(i) for i in line])
        heightmap = np.array(heightmap)
        
        low_points_heights = findLowPoints(heightmap)
        print('Ans A:',sum([point + 1 for point in low_points_heights]))

        low_points_loc = findLowPoints(heightmap, get_location=True)
        basin_sizes = findBasinSizes(heightmap, low_points_loc)
        sorted_basins = sorted(basin_sizes, reverse=True)
        print('Ans B:',np.prod(sorted_basins[0:3]))
        

        
