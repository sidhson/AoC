import load_data

dl = load_data.DataLoader(day=4)
data = dl.get_data()


def elf_task_contained_in(elf1, elf2):
    return (elf1[0] >= elf2[0] and elf1[1] <= elf2[1])


def elf_task_overlap(elf1, elf2):
    return (elf1[0] >= elf2[0] and elf1[0] <= elf2[1]) or (elf1[1] >= elf2[0] and elf1[1] <= elf2[1])


contains_count = 0

for line in data:
    elf1, elf2 = line.split(',')
    elf1 = [int(v) for v in elf1.split('-')]
    elf2 = [int(v) for v in elf2.split('-')]
    

    # # Part 1
    # if elf_task_contained_in(elf1, elf2) or elf_task_contained_in(elf2, elf1):
    #     contains_count += 1

    # Part 2
    if elf_task_overlap(elf1, elf2) or elf_task_overlap(elf2, elf1):
        contains_count += 1


print(contains_count)





