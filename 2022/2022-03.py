import load_data

dl = load_data.DataLoader(day=3)
data = dl.get_data()


import string

low_prio = dict(zip(string.ascii_lowercase, range(1,27)))
high_prio = dict(zip(string.ascii_uppercase, range(27,53)))

full_prio = dict(low_prio, **high_prio)


# Part 1
faulty_items = []
for rucksack in data:
    comp1 = rucksack[:len(rucksack)//2]
    comp2 = rucksack[len(rucksack)//2:]

    for itm in comp1:
        if itm in comp2:
            faulty_items.append(itm)
            break

points = 0
for itm in faulty_items:
    points += full_prio[itm]
print(f'Prio points sum: {points}')


# Part 2
badge_items = []
group = []
for rucksack in data:
    group.append(rucksack)

    if len(group) == 3:
        for itm in group[0]:
            if itm in group[1] and itm in group[2]:
                badge_items.append(itm)
                group = []
                break

points = 0
for itm in badge_items:
    points += full_prio[itm]
print(f'Badge points sum: {points}')