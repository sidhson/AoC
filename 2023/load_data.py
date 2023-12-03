from pathlib import Path


def get_data(day: str, as_list: bool=False) -> list:
    """Returns the input data. Split by rows if as_list is True."""
    year = '2023'
    input_path = Path(year) / f'input_{year}' / f'input_{year}-{day.zfill(2)}.txt'
    with open(input_path, 'r') as f:
        input = f.read()
        if as_list:
            return input.split('\n')
        else:
            return input
