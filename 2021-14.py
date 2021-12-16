import os

def insert_pairs_small(rules : dict, polymer : list, steps : int) -> list:
    for s in range(steps):
        # Find elements to add.
        add_elements = []
        for i in range(len(polymer)-1):
            pair = ''.join(polymer[i:i+2])
            if rules.get(pair) != None:    
                add_elements.append((rules.get(pair), i+1))
        # Add elements.
        for elem, i in reversed(add_elements):
            polymer.insert(i, elem)
    return polymer

def letter_frequency(letter_list : list) -> dict:
    global letter_set
    letter_map = {}
    for l in letter_set:
        letter_map[l] = 0
    for l in letter_list:
        letter_map[l] += 1
    return letter_map

def insert_pairs_big(rules : dict, polymer : list, steps : int) -> dict:
    pairs = []
    for i in range(len(polymer)-1):
        pairs.append(''.join(polymer[i:i+2]))

    pairs_mult = {}
    for pair in set(pairs):
        pairs_mult[pair] = pairs.count(pair)

    # Keeps track of the multiplicities of each pair of letters to avoid overflow.
    for _ in range(steps):
        new_pairs_mult = {}        
        for pair, mult in pairs_mult.items():
            new_polymer = insert_pairs_small(rules, list(pair), 1)
            for i in range(len(new_polymer)-1):
                new_pair = ''.join(new_polymer[i:i+2])
                if new_pair not in new_pairs_mult.keys():
                    new_pairs_mult[new_pair] = mult
                else:
                    new_pairs_mult[new_pair] += mult
        pairs_mult = new_pairs_mult.copy()
    
    # Sum frequencies for each letter.
    # Only considers the first letter to avoid counting doubles. 
    freq_map_big = {}
    for pair, count in pairs_mult.items():
        if pair[0] not in freq_map_big:
            freq_map_big[pair[0]] = count
        else:
            freq_map_big[pair[0]] += count
    freq_map_big[polymer[-1]] += 1 # Add last letter of original template.
    return freq_map_big

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        template, rules = f.read().split('\n\n')
        template = list(template)
        rule_map = {}
        for rule in rules.splitlines():
            pair, res = rule.split(' -> ')
            rule_map[pair] = res

        letter_set = set(rule_map.values())
        # Does the map contain all combinations? 
        for key in rule_map.keys():
            for k in list(key):
                letter_set.add(k) 
        print('Missing pairs:', 2**len(letter_set) - len(rule_map))

        ### Part A
        polymer_10_steps = insert_pairs_small(rule_map, template.copy(), 10)
        freq_map_10 = letter_frequency(polymer_10_steps)

        sorted_freq = sorted(freq_map_10.items(), key=lambda kv : (kv[1], kv[0]))
        least_common = sorted_freq[0]
        most_common = sorted_freq[-1]
        print('Ans A:', most_common[1] - least_common[1])

        ### Part B
        freq_map_40 = insert_pairs_big(rule_map, template.copy(), 40)
        sorted_freq = sorted(freq_map_40.items(), key=lambda kv : (kv[1], kv[0]))
        least_common = sorted_freq[0]
        most_common = sorted_freq[-1]
        print('Ans B:', most_common[1] - least_common[1])