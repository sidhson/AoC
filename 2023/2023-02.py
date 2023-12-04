from load_data import get_data

data = get_data(day='2', as_list=True)

# Part 1
rgb_config = {'red':12, 'green':13, 'blue':14}

def is_possible_game(subsets: str) -> bool:
    for subset in subsets.split('; '):
        for config in subset.split(', '):
            nbr, color = config.split()
            if int(nbr) > rgb_config[color]:
                return False
    return True

impossible_games = []
for game in data:
    id, subsets = game.split(': ')
    id = id.split()[1]
    if is_possible_game(subsets):
        impossible_games.append(int(id))

print(sum(impossible_games))


# Part 2 
def get_power(subsets: str) -> int:
    rgb_config = {'red':0, 'green':0, 'blue':0}
    for subset in subsets.split('; '):
        for config in subset.split(', '):
            nbr, color = config.split()
            if int(nbr) > rgb_config[color]:
                rgb_config[color] = int(nbr)
    return rgb_config['red']*rgb_config['green']*rgb_config['blue']

powers = []
for game in data:
    id, subsets = game.split(': ')
    id = id.split()[1]
    powers.append(get_power(subsets))
print(sum(powers))
