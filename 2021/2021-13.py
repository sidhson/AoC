import os
import numpy as np

def fold_paper(paper : np.array, axis : str, level : int):
    y_len, x_len = paper.shape

    if axis == 'y':
        new_paper = np.copy(paper[0:level,:])
        for row in range(level+1, y_len):
            for col in range(0, x_len):
                if paper[row, col] == 1:
                    new_paper[y_len-1-row, col] = 1
    else: 
        new_paper = np.copy(paper[:,0:level])
        for col in range(level+1, x_len):
            for row in range(0, y_len):
                if paper[row, col] == 1:
                    new_paper[row, x_len-1-col] = 1
    return new_paper

def fold_paper_multiple(paper : np.array, instructions : list, one_fold = True):
    for i, instruction in enumerate(instructions):
        paper = fold_paper(paper, instruction[0], instruction[1])
        if one_fold and i == 0: 
            break
    return paper

if __name__ == '__main__':
    filename = 'input_' + os.path.splitext(os.path.basename(__file__))[0] + '.txt'
    input_dir = os.path.join(os.path.dirname(__file__), 'input_2021', filename)
    with open(input_dir, 'r') as f:

        coordinates, instructions_raw = f.read().split('\n\n')
        coordinates = coordinates.splitlines()

        instructions = []
        for instruct in instructions_raw.splitlines():
            axis, nbr = instruct.strip().split(' ')[2].split('=')
            instructions.append((axis, int(nbr)))

        for i in range(2):
            axis, nbr = instructions[i]
            if axis == 'x':
                x_len = 2 * nbr + 1
            else: 
                y_len = 2 * nbr + 1

        paper = np.array([0] * y_len * x_len).reshape(y_len, x_len)
        for coordinate in coordinates:
            x, y = coordinate.strip().split(',')
            x = int(x)
            y = int(y)
            paper[y][x] = 1

        folded_paper = fold_paper_multiple(paper, instructions)
        print('Ans A:', np.sum(folded_paper)) 

        folded_paper = fold_paper_multiple(paper, instructions, False)
        folded_paper_print = np.array(['#' if i == 1 else '.' for i in folded_paper.flatten()]).reshape(folded_paper.shape)
        np.savetxt('2021-13-output.txt', folded_paper_print, fmt='%s')