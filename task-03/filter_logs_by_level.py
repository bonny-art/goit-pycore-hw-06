"""
Module for filtering logs by log level.

Includes:
- filter_logs_by_level: Filters log entries by a specified log level.
"""

from typing import List, Dict

from test_data import loaded_logs, expected_filtered_logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Filters a list of log dictionaries by the specified log level.

    Args:
        logs (List[Dict[str, str]]): A list of log dictionaries where each dictionary contains:
            - "date" (str): The date component of the log line.
            - "time" (str): The time component of the log line.
            - "level" (str): The log level component of the log line.
            - "message" (str): The message component of the log line.
        level (str): The log level to filter by. This should be one of the
        log levels present in the dictionaries.

    Returns:
        List[Dict[str, str]]: A list of log dictionaries that have the specified log level.
    """

    return [log for log in logs if log['level'] == level]

if __name__ == "__main__":
    # Example data
    filtered_logs = filter_logs_by_level(loaded_logs, "INFO")
    print(filtered_logs)

    # Test the function
    assert filtered_logs == expected_filtered_logs, (
        f"Test failed for filter_logs_by_level: got {filtered_logs}, "
        f"expected {expected_filtered_logs}"
    )

    print("All tests passed.")
