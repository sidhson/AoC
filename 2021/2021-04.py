import numpy as np
import os

## PART A
def singleBingo(board, sequence):
    for i in range(5):
        if (np.in1d(board[i,:],sequence).all() or np.in1d(board[:,i],sequence).all()):
            flat_board = board.flatten()
            unmarked = flat_board[np.in1d(flat_board, sequence, invert=True)]
            return (True, unmarked) # Return unmarked numbers.
    return (False, None)

def winBingo(boards, sequence):
    for i in range(5,len(sequence)): # Start with 5 numbers (minimum for win)
        for board in boards:
            win, unmarked = singleBingo(board, sequence[0:i])
            if (win):
                return np.sum(unmarked) * sequence[i-1] # End not included in slicing.

## PART B
def loseBingo(boards, sequence):
    i = 5
    while (i <= len(sequence) and len(boards) > 1):
        remove_ind = []
        for ind, board in enumerate(boards):
            win, unmarked = singleBingo(board, sequence[0:i])
            if (win):
                remove_ind.append(ind)

        for ind in reversed(remove_ind):
            boards.pop(ind)

        if (len(boards) == 1):
            flat_board = boards[0].flatten()
            unmarked = flat_board[np.in1d(flat_board, sequence[0:i+1], invert=True)]
            return np.sum(unmarked) * sequence[i]
        i += 1

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:
        # Store number sequence as np array.
        numbers_drawn = np.array(f.readline().strip().split(',')).astype(np.int32)
        
        # Store boards as np matricies.
        boards = f.read().split("\n\n")
        np_boards = [np.array(board.split()).astype(np.int32).reshape(5,5) for board in boards]

        # Find the winning board.
        print('Ans A: ', winBingo(np_boards, numbers_drawn))
        print('Ans B: ', loseBingo(np_boards, numbers_drawn))
