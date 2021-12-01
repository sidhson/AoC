import os
filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)

with open(input_dir, 'r') as f:
    input = f.readlines()
    input = [int(line.strip()) for line in input]

# Solution start
inc_count = 0
cur_measure = input[0]

for measure in input:
    if measure > cur_measure:
        inc_count += 1
    cur_measure = measure

print(inc_count)