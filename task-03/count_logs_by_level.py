"""
Module for counting log lines by level.

Includes:
- count_logs_by_level: Counts occurrences of each log level in a list of log dictionaries.
"""

from collections import Counter
from typing import Dict, List

from test_data import loaded_logs, expected_counts

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Counts the number of log lines for each log level in a list of log dictionaries.

    Args:
        logs (List[Dict[str, str]]): A list of log dictionaries where each dictionary contains:
            - "date" (str): The date component of the log line.
            - "time" (str): The time component of the log line.
            - "level" (str): The log level component of the log line.
            - "message" (str): The message component of the log line.

    Returns:
        Dict[str, int]: A dictionary where the keys are log levels and 
        values are the number of log lines for each log level.
    """

    levels = [log['level'] for log in logs]
    return dict(Counter(levels))

if __name__ == "__main__":
    # Example data
    log_counts = count_logs_by_level(loaded_logs)
    print(log_counts)

    # Test the function
    assert log_counts == expected_counts, (
        f"Test failed: expected {expected_counts}, got {log_counts}"
    )
    print("All tests passed.")
