from pathlib import Path


class DataLoader:
    '''Loads the data of a specified day (2022).'''
    def __init__(self, day: int) -> None:
        self.day = day

    def get_data(self, as_list: bool) -> list:
        '''
        Returns the input data. Split by rows if as_list is True.
        '''
        input_path = Path() / '2022' / 'input_2022' / f'input_2022-{self.day}.txt'
        with open(input_path, 'r') as f:
            input = f.read()
            if as_list:
                return input.split('\n')
            else:
                return input
