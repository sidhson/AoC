import load_data

dl = load_data.DataLoader(day=5)
data = dl.get_data(as_list=False)


import re

starting_stacks, rearrangement_procedure = data.split('\n\n')
rearrangement_procedure = rearrangement_procedure.split('\n')

starting_stacks = starting_stacks.split('\n')
stack_nbrs = starting_stacks.pop(-1)


stacks = [[] for _ in stack_nbrs.strip().split()]

# Construct stating creates structure
for row in reversed(starting_stacks):
    for i, crate in enumerate(row[1::4]):
        if crate != ' ':
            stacks[i] += crate

# Perform rearrangement procedure
for move in rearrangement_procedure:
    move = re.sub('[^0-9 ]', '', move)
    move = [int(m) for m in move.split()]
    nbr_crates, from_stack, to_stack = move

    # # Part 1
    # for _ in range(nbr_crates):
    #     stacks[to_stack-1] += stacks[from_stack-1].pop()
    
    # Part 2
    moved_crates = []
    for _ in range(nbr_crates):
        moved_crates += stacks[from_stack-1].pop()
    stacks[to_stack-1] += reversed(moved_crates)

top_crates = ''
for s in stacks:
    top_crates += s[-1]
print(top_crates)



    
