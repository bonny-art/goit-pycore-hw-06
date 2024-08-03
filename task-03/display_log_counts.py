"""
Module for displaying log counts in a tabular format.

Includes:
- display_log_counts: Prints log counts by level in a formatted table.
"""

from typing import Dict
from colorama import Fore, Style, init
from test_data import expected_counts as example_counts
from test_data import LOG_SELECTED

init(autoreset=True)

def display_log_counts(counts: Dict[str, int], highlight_level: str = None):
    """
    Displays the log counts for each log level in a tabular format. Optionally
    highlights a specific log level.

    Args:
        counts (Dict[str, int]): A dictionary where the keys are log levels and
                                 the values are the number of log lines for each
                                 log level.
        highlight_level (str, optional): The log level to highlight. If provided,
                                         this level will be displayed in green. Defaults to None.
    """

    print(f"{'Рівень логування':<20}| {'Кількість':<10}")
    print('-' * 32)

    def format_line(level, count):
        if highlight_level and level.upper() == highlight_level:
            return f"{Fore.GREEN}{level:<20}{Style.RESET_ALL}| {Fore.GREEN}{count:<10}"

        return f"{level:<20}| {count:<10}"

    formatted_lines = map(lambda item: format_line(*item), counts.items())

    for line in formatted_lines:
        print(line)

if __name__ == "__main__":
    # Example data
    display_log_counts(example_counts, LOG_SELECTED)
    print()
    display_log_counts(example_counts)
