"""
Module for printing logs of a specified level.

Includes:
- print_logs_by_level: Prints logs of a specified level in a formatted manner.
"""

from typing import List, Dict
from filter_logs_by_level import filter_logs_by_level

def print_logs_by_level(logs: List[Dict[str, str]], level: str) -> None:
    """
    Prints the logs of a specified level in a formatted manner.

    Args:
        logs (List[Dict[str, str]]): A list of log dictionaries where each dictionary contains:
            - "date" (str): The date component of the log line.
            - "time" (str): The time component of the log line.
            - "level" (str): The log level component of the log line.
            - "message" (str): The message component of the log line.
        level (str): The log level to filter and print.
    """
    filtered_logs: List[Dict[str, str]] = filter_logs_by_level(logs, level)

    if filtered_logs:
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"No logs found for level '{level}'")
