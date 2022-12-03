from pathlib import Path


class DataLoader:
    '''Loads the data of a specified day (2022).'''
    def __init__(self, day: int) -> None:
        self.day = day

    def get_data(self) -> list:
        '''Returns the input data split by rows.'''
        input_path = Path() / '2022' / 'input_2022' / f'input_2022-{self.day}.txt'
        with open(input_path, 'r') as f:
            return f.read().split('\n')