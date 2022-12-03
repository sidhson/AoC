import load_data

dl = load_data.DataLoader(day=1)
data = dl.get_data()


cals_list = [0]
pos = 0
for cals in data:
    if not cals:
        pos += 1
        cals_list.append(0)
    else:
        cals_list[pos] += int(cals)


print(f'Max elf cals: {max(cals_list)}')

cals_list.sort(reverse=True)
print(f'Top 3 elf cals sum: {sum(cals_list[:3])}')
