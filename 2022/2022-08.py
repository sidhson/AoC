import load_data

dl = load_data.DataLoader(day=8)
data = dl.get_data(as_list=True)


import numpy as np

tree_matrix = []

for row in data:
    tree_matrix.append([int(t) for t in row])

tree_matrix = np.array(tree_matrix)
visibility_matrix = np.zeros(tree_matrix.shape) # Stores 1 for visibile and 0 for not visible.
scenic_score_matrix = np.zeros(tree_matrix.shape) # Stores the scenic score for each tree location. 

n_rows, n_cols = tree_matrix.shape

# Set edges as visible. 
for row in range(n_rows):
    visibility_matrix[row, 0] = 1
    visibility_matrix[row, n_cols-1] = 1
for col in range(n_cols):
    visibility_matrix[0, col] = 1
    visibility_matrix[n_rows-1, col] = 1

# Part 1
# Skip outermost trees.
for row in range(1,n_rows-1):
    for col in range(1,n_cols-1):
        # Check up
        current_tree = tree_matrix[row, col]
        if current_tree > max(tree_matrix[:row, col]):
            visibility_matrix[row, col] = 1
        # Check down
        elif current_tree > max(tree_matrix[row+1:, col]):
            visibility_matrix[row, col] = 1
        # Check left
        elif current_tree > max(tree_matrix[row, :col]):
            visibility_matrix[row, col] = 1
        # Check right
        elif current_tree > max(tree_matrix[row,col+1:]):
            visibility_matrix[row, col] = 1
            
print(f'Visible trees: {visibility_matrix.sum()}')


# Part 2
def check_scenic_visibility(current_tree, tree_sequence):
    # If edge tree
    if len(tree_sequence) == 0:
        return 0
    
    highest_tree = 0
    n_trees = 0
    for t in tree_sequence:
        n_trees += 1
        if t >= current_tree:
            break
        if t > highest_tree:
            highest_tree = t
    return n_trees

for row in range(0,n_rows):
    for col in range(0,n_cols):
        current_tree = tree_matrix[row, col]
        trees_in_directions = []
        
        # Check up
        n_trees_seen = check_scenic_visibility(current_tree, np.flip(tree_matrix[:row, col]))
        trees_in_directions.append(n_trees_seen)
        # Check down
        n_trees_seen = check_scenic_visibility(current_tree, tree_matrix[row+1:, col])
        trees_in_directions.append(n_trees_seen)
        # Check left
        n_trees_seen = check_scenic_visibility(current_tree, np.flip(tree_matrix[row, :col]))
        trees_in_directions.append(n_trees_seen)
        # Check right
        n_trees_seen = check_scenic_visibility(current_tree, tree_matrix[row, col+1:])
        trees_in_directions.append(n_trees_seen)

        # Compute scenic score
        scenic_score_matrix[row, col] = np.prod(trees_in_directions)


print(f'Max scenic score: {scenic_score_matrix.max()}')
