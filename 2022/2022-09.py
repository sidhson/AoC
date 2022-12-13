import load_data

dl = load_data.DataLoader(day=9)
data = dl.get_data(as_list=True)

from dataclasses import dataclass
import numpy as np
import math


@dataclass
class RopePart:
    '''Stores the position of head/tail from bottom left corner.'''
    x: int
    y: int

def move_rope_knot(head: RopePart, tail: RopePart) -> None:
    # Move vertical direction. 
    if abs(head.y - tail.y) > 1:
        tail.y += int(math.copysign(1, head.y - tail.y))
        if head.x != tail.x: # Diagonal move if not on same x coordinate
            tail.x += int(math.copysign(1, head.x - tail.x))

    # Move horizontal direction. 
    elif abs(head.x - tail.x) > 1:
        tail.x += int(math.copysign(1, head.x - tail.x))
        if head.y != tail.y: # Diagonal move if not on same y coordinate
            tail.y += int(math.copysign(1, head.y - tail.y))


field_dim = (10_000,10_000)
rope_state_matrix = np.zeros(field_dim)
visited_matrix_p1 = np.zeros(field_dim)
visited_matrix_p2 = np.zeros(field_dim)

# Part 1
head = RopePart(0,0)
tail = RopePart(0,0)
visited_matrix_p1[head.x, head.y] = 1

# Part 2
rope_parts = []
rp = RopePart(0,0)
for _ in range(10):
    rp = RopePart(0,0)
    rope_parts.append(rp)

head = rope_parts[0]
visited_matrix_p2[head.x, head.y] = 1

for move in data:
    dir, steps = move.split()

    for _ in range(int(steps)):
        if dir == 'U':
            head.y += 1
        elif dir == 'D':
            head.y -= 1
        elif dir == 'R':
            head.x += 1
        elif dir == 'L':
            head.x -= 1

        # Part 1
        move_rope_knot(head, tail)
        visited_matrix_p1[tail.x, tail.y] = 1

        # Part 2
        for i in range(len(rope_parts)-1):
            move_rope_knot(rope_parts[i], rope_parts[i+1])        
        visited_matrix_p2[rope_parts[-1].x, rope_parts[-1].y] = 1


print(f'spots visited by tail (short rope): {visited_matrix_p1.sum()}')
print(f'spots visited by tail (long rope): {visited_matrix_p2.sum()}')
