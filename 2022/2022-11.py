import load_data

dl = load_data.DataLoader(day=11)
data = dl.get_data(as_list=False)


from dataclasses import dataclass
import re

# NUMBER_OF_ROUNDS = 20
NUMBER_OF_ROUNDS = 10_000

monkey_info = data.split('\n\n')

@dataclass
class Monkey:
    items: list
    operation: None
    operation_nbr: int
    test_div_by: int
    to_monkey_true: int
    to_monkey_false: int
    items_inspected: int

    def play_round(self):
        '''Update the monkey's items.'''
        nbr_of_items = len(self.items)
        for i in range(nbr_of_items):
            self.items_inspected += 1
            item = self.items.pop(0)
            new_worry_level = self.operation(item, self.operation_nbr)

            # new_worry_level = new_worry_level // 3 # NOTE: Part 1 => reduce worry levels.
            new_worry_level = new_worry_level % mod_all_monkeys # NOTE: Part 2 => keep levels manageable

            if new_worry_level % self.test_div_by == 0:
                monkey_list[self.to_monkey_true].items.append(new_worry_level)
            else:
                monkey_list[self.to_monkey_false].items.append(new_worry_level)


# Generate the monkeys
monkey_list = []
for monkey_info_i in monkey_info:
    monkey_info_i = monkey_info_i.split('\n')
    monkey_nbr = int(re.sub('[^0-9]', '', monkey_info_i[0]))

    starting_items = list(monkey_info_i[1].split(': ')[1].split(', '))
    starting_items = [int(v) for v in starting_items]

    if monkey_info_i[2].split(' = ')[1] == 'old * old':
        op_nbr = None
        operation = lambda x, op_nbr: x**2
    
    elif '+' in monkey_info_i[2]:
        op_nbr = int(re.sub('[^0-9]', '', monkey_info_i[2]))
        operation = lambda x, op_nbr: x + op_nbr
    
    elif '*' in monkey_info_i[2]:
        op_nbr = int(re.sub('[^0-9]', '', monkey_info_i[2]))
        operation = lambda x, op_nbr: x * op_nbr

    test_divisible_by = int(monkey_info_i[3].split()[-1])
    
    test_if_true_to_monkey = int(monkey_info_i[4].split()[-1])
    test_if_false_to_monkey = int(monkey_info_i[5].split()[-1])

    monkey = Monkey(
        items=starting_items,
        operation=operation,
        operation_nbr=op_nbr,
        test_div_by=test_divisible_by,
        to_monkey_true=test_if_true_to_monkey,
        to_monkey_false=test_if_false_to_monkey,
        items_inspected=0
    )
    monkey_list.append(monkey)


# Mod operator to handle large numbers in part 2
mod_all_monkeys = 1
for m in monkey_list:
    mod_all_monkeys *= m.test_div_by


# Run the game!
for round in range(NUMBER_OF_ROUNDS):
    if round % 1000 == 0: print(f'At round {round}. Keep it going!')
    for monkey_nbr in range(len(monkey_list)):
        monkey_list[monkey_nbr].play_round()

for i, m in enumerate(monkey_list):
    print(m.items_inspected, 'by monkey', i)

inspected_items = [m.items_inspected for m in monkey_list]
inspected_items.sort()
top_inspected_items = inspected_items[-2:]

print(top_inspected_items)
print(top_inspected_items[0]*top_inspected_items[1])
