from load_data import get_data
import re

data = get_data(day='1', as_list=True)

# Part 1
numbers = [re.sub('[^0-9]','',line) for line in data]
numbers = [int(nbr[0] + nbr[-1]) for nbr in numbers]
print(sum(numbers))


# Part 2
def get_first_nbr(line: str, nbrs_dict: dict) -> str:
    for i in range(len(line)):
        for nbr_len in range(3,6): # one, two, three etc are len 3-5
            nbr_str = line[i:i+nbr_len]
            if nbr_str in nbrs_dict.keys():
                return nbr_str

def get_last_nbr(line: str, nbrs_dict: dict) -> str:
    for i in range(len(line)):
        for nbr_len in range(3,6): # one, two, three etc are len 3-5
            nbr_str = line[len(line)-i-nbr_len:len(line)-i]
            if nbr_str in nbrs_dict.keys():
                return nbr_str

nbrs_dict = dict(zip(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], [str(i) for i in list(range(1,10))] ))

numbers = []
for line in data:
    new_line: str = line
    for nbr_str, nbr in nbrs_dict.items():
        new_line = new_line.replace(nbr, nbr_str)

    first_nbr = get_first_nbr(new_line, nbrs_dict)
    last_nbr = get_last_nbr(new_line, nbrs_dict)
    
    numbers.append(int(nbrs_dict[first_nbr] + nbrs_dict[last_nbr]))

print(sum(numbers))
