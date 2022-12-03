import load_data

dl = load_data.DataLoader(day=2)
data = dl.get_data()


weapon_point_p1 = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

game_point_p1 = {
    'A X': 3, # draw
    'B Y': 3,
    'C Z': 3,
    
    'A Y': 6, # win
    'B Z': 6,
    'C X': 6,

    'A Z': 0, # lost
    'B X': 0,
    'C Y': 0
}

game_point_p2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

weapon_point_p2 = {
    'A X': 3, # rock + lose, sicssor
    'B X': 1, # paper + lose, rock
    'C X': 2, # scissor + lose, paper
    
    'A Y': 1, # rock + draw, rock
    'B Y': 2,
    'C Y': 3,

    'A Z': 2, # rock + win, paper
    'B Z': 3, # paper + win, scissor
    'C Z': 1
}
points = 0

for game in data:
    _, choice = game.split()
    
    # Part 1
    # points += weapon_point_p1[choice]
    # points += game_point_p1[game]

    # Part 2
    points += game_point_p2[choice]
    points += weapon_point_p2[game]


print(f'Total points from games: {points}')