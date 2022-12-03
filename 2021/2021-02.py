import os

## PART A
def sumPath(input):
    sum_horizontal = 0
    sum_depth = 0
    for move in input:
        dir, nbr = move.split()
        nbr = int(nbr)
        if dir == 'forward':
            sum_horizontal += nbr
        elif dir == 'down':
            sum_depth += nbr
        else:
            sum_depth -= nbr
    return (sum_depth, sum_horizontal)

## PART B
def sumPathAim(input):
    sum_horizontal = 0
    sum_depth = 0
    aim = 0
    for move in input:
        dir, nbr = move.split()
        nbr = int(nbr)
        if dir == 'forward':
            sum_horizontal += nbr
            sum_depth += nbr*aim
        elif dir == 'down':
            aim += nbr
        else:
            aim -= nbr
    return (sum_depth, sum_horizontal)


if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = f.readlines()
        input = [line.strip() for line in input]
    
    # final_path = sumPath(input) # Part A
    final_path = sumPathAim(input) # Part B
    print('Final depth: ', final_path[0], ', Final horizontal: ', final_path[1])
    print('Ans: ', final_path[0]*final_path[1])

    
    