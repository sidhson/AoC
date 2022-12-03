import os
import numpy as np

def simulate_steps(grid : np.array, steps : int, all_flash_one_round = False):
    """
    Energy is stored in range [0,9]. 
    Energy of 10 will flash this round. 
    Energy of -1 has already flashed this round.
    """
    to_flash = []
    count = 0
    allowed_range = set((i,j) for i in range(len(grid)) for j in range(len(grid[0])))

    for step in range(steps):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j], new_flash = increase_energy(grid[i][j])
                if new_flash: to_flash.append((i,j))

        while len(to_flash) > 0:
            count += 1
            flash_i, flash_j = to_flash.pop()
            grid[flash_i][flash_j] = -1

            # Increase surrounding energy.
            for i in range(flash_i-1,flash_i+2):
                for j in range(flash_j-1,flash_j+2):
                    if ((i,j) in allowed_range):
                        grid[i][j], new_flash = increase_energy(grid[i][j])
                        if new_flash: to_flash.append((i,j))

        # Reset flashed octopuses to 0. 
        count_single_round = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = 0
                    count_single_round += 1
        if all_flash_one_round and count_single_round == 10*10:
            return step + 1

    return count

def increase_energy(energy : int):
    flash = False
    if not (energy == -1 or energy == 10):
        energy += 1
        if energy == 10:
            flash = True
    return energy, flash

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = []    
        for line in f.readlines():
            for i in line.strip():        
                input.append(int(i))
        input = np.array(input).reshape(10,10)

        number_of_flashes = simulate_steps(input.copy(), 100, False)
        print('Ans A:', number_of_flashes)

        sync_step = first_synchronized_flash = simulate_steps(input.copy(), 500, True)
        print('Ans B:', sync_step)