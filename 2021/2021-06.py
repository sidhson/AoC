import os

def growFish(fishes, days):
    for _ in range(days):
        new_fish = 0
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                new_fish += 1
            else:
                fishes[i] -= 1

        fishes.extend([8] * new_fish)
    return fishes

def growLargePopulation(fishes, days):
    compressed_fish = [0] * 9 # Possible days left for a fish.
    for fish in fishes:
        compressed_fish[fish] += 1
    
    for _ in range(days):
        new_fish = compressed_fish[0]
        for i in range(len(compressed_fish)-1):
            compressed_fish[i] = compressed_fish[i+1]

        compressed_fish[6] += new_fish # Fish reset at day 6
        compressed_fish[-1] = new_fish # New fish spawned at day 8
    return compressed_fish


if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        start_fish = f.readline().strip().split(',')
        start_fish = [int(i) for i in start_fish]
        
        
        end_fish = growFish(start_fish.copy(), 80)
        print('Ans A:', len(end_fish))

        end_large_population = growLargePopulation(start_fish, 256)
        print('Ans B:', sum(end_large_population))


        