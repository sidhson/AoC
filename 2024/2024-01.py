from load_data import get_data
import pandas as pd


input_data = get_data(2024,1,True)

locations = pd.DataFrame([s.split() for s in input_data], columns=['left','right'])
left = locations.left.astype(int)
right = locations.right.astype(int)


# Part 1
locations.left = sorted(left)
locations.right = sorted(right)

locations['dist'] = locations.apply(lambda r: abs(r['left']-r['right']), axis=1)
print(locations.dist.sum())


# Part 2
right_value_map = right.value_counts().to_dict()

total = 0
for left_val in list(left):
    r_factor = right_value_map.get(left_val)
    if r_factor: 
        total += (left_val * int(r_factor))
print(total)

# alt 1-liner:
print(sum([left_val * right_value_map[left_val] for left_val in left if left_val in right_value_map.keys()]))
