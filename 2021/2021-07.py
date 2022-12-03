import os

def minimizeFuel(position, min_pos, max_pos, const):
    fuel_consumptions = []
    for pos in range(min_pos, max_pos+1):
        fuel_consumptions.append(getFuelConsumption(position, pos, const))
    min_fuel = min(fuel_consumptions)
    return min_fuel, fuel_consumptions.index(min_fuel)

def getFuelConsumption(current_pos, goal_pos, const=True):
    total_fuel = 0
    for crab in current_pos:
        if const:
            total_fuel += abs(goal_pos - crab)
        else:
            total_fuel += sum(range(1,abs(goal_pos - crab)+1))
    return total_fuel

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        init_pos = f.readline().strip().split(',')
        init_pos = [int(i) for i in init_pos]

    print('Max:', max(init_pos))
    print('Min:', min(init_pos))

    min_fuel, pos = minimizeFuel(init_pos, 0, 2000, True)
    print('Ans A: ', 'Min fuel consumption:', min_fuel, 'Pos:', pos)

    min_fuel, pos = minimizeFuel(init_pos, 0, 2000, False)
    print('Ans B: ', 'Min fuel consumption:', min_fuel, 'Pos:', pos)
        
        


        