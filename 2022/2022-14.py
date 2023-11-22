import load_data

dl = load_data.DataLoader(day=14)
data = dl.get_data(as_list=True)


from dataclasses import dataclass
import numpy as np

xdim = 1000
ydim = 1000
cave_map = np.array([['.' for _ in range(xdim)] for _ in range(ydim)])

@dataclass
class Sand:
    x: int
    y: int

    def move(self):
        '''
        Moves a grain of sand until it stops or runs out of bounds.
        Returns True if stopped at rest and False if out of bounds.
        '''
        while True:
            if self.y+1 >= ydim:
                return False
                
            elif cave_map[self.x,self.y+1] == '.':
                self.y += 1
            elif cave_map[self.x-1,self.y+1] == '.':
                self.y += 1
                self.x -= 1
            elif cave_map[self.x+1,self.y+1] == '.':
                self.y += 1
                self.x += 1
            else: 
                cave_map[self.x, self.y] = 'o'
                return True


max_y = 0 # Part 2

# Draw the initial cave rock strucutre. 
for line in data: 
    locations = line.split(' -> ')
    locations = [[int(l) for l in loc.split(',')] for loc in locations] 

    for i in range(len(locations)-1):
        x1, y1 = locations[i]
        x2, y2 = locations[i+1]

        cave_map[x1:x2+1, y1:y2+1] = '#'
        cave_map[x2:x1+1, y2:y1+1] = '#'

        for y in [y1, y2]:
            if y > max_y:
                max_y = y1

# Part 2: Draw extra floor.
cave_map[:,max_y+2] = '#'


sand_moved = True
sand_count = 0

while sand_moved: # Did any sand move? 
    if cave_map[500,0] == 'o':
        break

    s = Sand(x=500,y=0)
    sand_moved = s.move()
    if sand_moved:
        sand_count += 1


print(f'sand count: {sand_count}')

keys, vals = np.unique(cave_map, return_counts=True)
for k,v in zip(keys,vals):
    print(k, v)
