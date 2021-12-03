import os

## PART A
def binarySum(input):
    count_of_ones = [0 for _ in range(len(input[0]))]
    gamma = ''
    epsilon = ''

    for entry in input:
        for i, nbr in enumerate(entry):
            count_of_ones[i] += int(nbr)
    
    input_len = len(input)
    for bit in count_of_ones:
        if bit > input_len / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    return (gamma,epsilon)

## Part B
def binaryFilter(input, bit): 
    values = input
    i = 0
    while i < len(input[0]):
        values_ones = []
        values_zeros = []
        for entry in values:
            if entry[i] == bit:
                values_ones.append(entry)
            else:
                values_zeros.append(entry)

        if bit == '1':
            if len(values_ones) >= len(values_zeros):
                values = values_ones
            else:
                values = values_zeros
        else: 
            if len(values_ones) <= len(values_zeros):
                values = values_ones
            else:
                values = values_zeros

        if len(values) == 1:
            return values[0]
        i += 1

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = f.read().splitlines()
    
    # Part A
    gamma, epsilon = binarySum(input)
    print('Ans A: ', int(gamma, base=2)*int(epsilon, base=2))

    # Part B
    oxygen = binaryFilter(input, bit='1')
    co2 = binaryFilter(input, bit='0')
    print('Ans B: ', int(oxygen, base=2)*int(co2, base=2))


    
    