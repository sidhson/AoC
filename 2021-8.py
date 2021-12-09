import os

def countUniqueValues(sequence : list):
    unique_values = set([2, 3, 4, 7]) # Digits 1,7,4,8
    count = 0
    for entry in sequence:
        for digit in entry:
            if len(digit) in unique_values:
                count += 1
    return count

def decodeAllOutputs(signals : list, outputs : list):
    decoders = [decodeSignal(s) for s in signals]
    total = 0
    for decoder, o in zip(decoders, outputs):
        nbrs = [str(decoder.index(digit)) for digit in o]
        total += int(''.join(nbrs))
    return total

def decodeSignal(signal : list):
    decoded_numbers = [''] * 10 # index corresponds to digit
    remaining_r1 = []
    remaining_r2 = []
    
    for digit in signal:
        # First decode the unique values
        if len(digit) == 2:
            decoded_numbers[1] = digit
        elif len(digit) == 3:
            decoded_numbers[7] = digit
        elif len(digit) == 4:
            decoded_numbers[4] = digit
        elif len(digit) == 7:
            decoded_numbers[8] = digit
        else:
            remaining_r1.append(digit)

    for digit in remaining_r1:
        # Then decode 0, 6, 9 (all of length 6)
        if len(digit) == 6:
            if all(d in [*digit] for d in [*decoded_numbers[4]]): # 4 is contained in 9.
                decoded_numbers[9] = digit
            elif all(d in [*digit] for d in [*decoded_numbers[7]]): # 7 in contained in 0. 
                decoded_numbers[0] = digit
            else:
                decoded_numbers[6] = digit
        else:
            remaining_r2.append(digit)
    
    for digit in remaining_r2:
        # Remaining digits are all length five.
        if all(d in [*digit] for d in [*decoded_numbers[1]]): # 1 is contained in 3.
            decoded_numbers[3] = digit
        elif all(d in [*decoded_numbers[6]] for d in [*digit]): # 5 is contained in 6. 
            decoded_numbers[5] = digit
        else:
            decoded_numbers[2] = digit
            
    return decoded_numbers


if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:

        outputs = []
        signals = []
        for line in f:
            left_input, right_input = line.strip().split(' | ')
            outputs.append(right_input.split())
            signals.append(left_input.split())
        
        # Sort all of the digit entries. 
        for i in range(len(signals)):
            for j in range(len(signals[0])):
                signals[i][j] = ''.join(sorted(signals[i][j]))
            for j in range(len(outputs[0])):
                outputs[i][j] = ''.join(sorted(outputs[i][j]))
        
        nbr_unique = countUniqueValues(outputs)
        print('Ans A:', nbr_unique)

        sum_outputs = decodeAllOutputs(signals, outputs)
        print('Ans B:', sum_outputs)
    