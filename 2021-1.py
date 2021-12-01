import os

## PART A
def countIncrease(input):
    inc_count = 0
    cur_measure = input[0]

    for measure in input:
        if measure > cur_measure:
            inc_count += 1
        cur_measure = measure
    return inc_count

## PART B
def slidingAverage(input):
    new_measures = []
    for i in range(0,len(input)-2):
        new_measure = sum(input[i:i+3])
        new_measures.append(new_measure)
    return new_measures

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = f.readlines()
        input = [int(line.strip()) for line in input]
    
    # Part A
    print('Ans part A:',countIncrease(input))
    
    # Part B
    new_input = slidingAverage(input)
    print('Ans part B:',countIncrease(new_input))