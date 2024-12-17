from pathlib import Path
from datetime import datetime


def get_data(year: int, day: int, as_list: bool = False) -> list:
    """
    Returns the input data. Split by rows if as_list is True.
    """
    assert year in range(2021, datetime.now().year+1), "Do not look into the future!"
    assert day in range(1, 25+1), "Do not look into the future!"

    input_path = Path() / str(year) / f"input_{year}" / f"input_{year}-{day:02}.txt"
    assert input_path.exists(), "Path not found, has data been loaded?"
    
    with open(input_path, "r") as f:
        input = f.read()
        if as_list:
            return input.split("\n")
        else:
            return input
