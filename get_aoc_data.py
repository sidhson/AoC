import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load env variables
load_dotenv()

# Constants
BASE_URL = "https://adventofcode.com"


def fetch_aoc_input_for_day(
    year: int, day: int, session_cookie: str, output_dir: str = None
) -> str:
    """
    Fetches Advent of Code input data for a given year and day.

    Parameters:
        year (int): The year of the challenge.
        day (int): The day of the challenge (1-25).
        session_cookie (str): Your session cookie for AoC.
        output_dir (str): Directory to save the input file.

    Returns:
        str: The path to the saved input file.
    """
    # Validate day
    if day < 1 or day > 25:
        raise ValueError("Day must be between 1 and 25.")

    # Ensure output directory exists
    if output_dir is None:
        output_dir = Path() / str(year) / f"input_{year}"
    os.makedirs(output_dir, exist_ok=True)

    # Define file path
    file_name = f"input_{year}-{day:02}.txt"
    file_path = os.path.join(output_dir, file_name)

    # Skip download if input already exists
    if os.path.exists(file_path):
        print(f"Input for day {day} already exists at {file_path}.")
        return file_path

    # Define URL and headers
    url = f"{BASE_URL}/{year}/day/{day}/input"
    headers = {"User-Agent": "AoC Input Fetcher by <fredrik.sidh(at)hotmail>"}
    cookies = {"session": session_cookie}

    # Fetch input data
    print(f"Fetching input for year {year}, day {day}...")
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        # Save to file
        with open(file_path, "w") as f:
            f.write(response.text.strip())
        print(f"Input successfully saved to {file_path}.")
        return file_path
    else:
        raise Exception(
            f"Failed to fetch input: {response.status_code} - {response.reason}"
        )


if __name__ == "__main__":
    import argparse

    # Load session cookie from .env
    session_cookie = os.getenv("AOC_SESSION")
    if not session_cookie:
        raise Exception(
            "Session cookie not found in .env file. Please set AOC_SESSION."
        )

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Fetch Advent of Code input data.")
    parser.add_argument("--year", type=int, help="Year of the Advent of Code challenge")
    parser.add_argument("--day", type=int, help="Day of the challenge (1-25)")
    parser.add_argument("--output", type=str, help="Output directory for input files")
    args = parser.parse_args()
    print(args)

    try:
        fetch_aoc_input_for_day(args.year, args.day, session_cookie, args.output)
    except Exception as e:
        print(f"Error: {e}")
