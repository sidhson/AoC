import load_data

dl = load_data.DataLoader(day=10)
data = dl.get_data(as_list=True)


CYCLE_FREQ = 40
cycle_freq_values = []

cycle = 0
current_value = 1

display = [[] for _ in range(6)]

def draw_pixel():
    '''Draw a single pixel based on current value.'''
    global cycle, current_value, display
    row = cycle // CYCLE_FREQ
    position_drawn = cycle % CYCLE_FREQ
    if position_drawn >= current_value-1 and position_drawn <= current_value+1:
        display[row].append('#')
    else: 
        display[row].append('.')


def increment_cycle():
    '''Increment cycle and store values at specific cycles.'''
    global cycle, cycle_freq_values, current_value
    draw_pixel()
    cycle += 1
    if (cycle + 20) % CYCLE_FREQ == 0:
        cycle_freq_values.append(current_value)


for instruction in data:
    if instruction == 'noop':
        increment_cycle()
    else:
        next_value = int(instruction.split()[1])
        increment_cycle()
        increment_cycle()
        current_value += next_value

print(f'total cycles: {cycle}')
print(f'cycle marks: {cycle_freq_values}')

# Part 1
total = 0
for i, val in enumerate(cycle_freq_values):
    strength = (20 + 40*i)*val
    total += strength
print(total)

# Part 2
for row in display:
    print(''.join(row))