import os

def find_corrupted(lines : list, illegal_chars : set, closing_to_opening : dict):
    corrupted_chars = []
    incomplete = lines.copy()
    for line in lines:
        open_chars = [line[0]]
        for i in range(1,len(line)):
            char = line[i]    
            if char in illegal_chars: # Closing character. 
                if closing_to_opening[char] == open_chars[-1]:
                    open_chars.pop() # Matching closing character. 
                else:
                    corrupted_chars.append(char)
                    incomplete.remove(line)
                    break
            else: # Opening character.
                open_chars.append(char)

    return corrupted_chars, incomplete

def find_closing(incomplete : list, illegal_chars : set, opening_to_closing : dict):
    closing_sequences = []
    
    # First determine the "unclosed" characters. 
    for line in incomplete:
        open_chars = [line[0]]
        for i in range(1,len(line)):
            char = line[i]
            if char in illegal_chars: # Closing character always correct. 
                open_chars.pop()
            else: # Opening character.
                open_chars.append(char)

        # Open characters are now retrieved 
        closing_sequence = []
        for char in reversed(open_chars):
            closing_sequence.append(opening_to_closing[char])
        closing_sequences.append(closing_sequence)

    return closing_sequences

def calculate_scores(sequences : list):
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for s in sequences:
        score = 0
        for char in s:
            score = 5 * score + score_map[char]
        scores.append(score)
    return scores

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        input = [line.strip() for line in f.readlines()]
    
    illegal_chars = set([')', ']', '}', '>'])
    illegal_scores = {')' : 3, ']' : 57,  '}' : 1197, '>' : 25137}

    closing_to_opening = {')':'(', ']':'[', '}':'{', '>':'<'}
    opening_to_closing = {open:close for close,open in closing_to_opening.items()}

    corruped_chars, incomplete = find_corrupted(input, illegal_chars, closing_to_opening)
    print('Ans A:', sum([illegal_scores[c] for c in corruped_chars]))
    
    closing_sequences = find_closing(incomplete, illegal_chars, opening_to_closing)
    sorted_scores = sorted(calculate_scores(closing_sequences))
    print('Ans B:', sorted_scores[int(len(sorted_scores)/2)])
