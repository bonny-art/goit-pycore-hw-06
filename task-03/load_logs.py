"""
Module for loading and parsing log files into dictionaries.
"""

import sys
from typing import List, Dict
from pathlib import Path
from parse_log_line import parse_log_line

from test_data import loaded_logs as expected_logs

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Loads log lines from a file and parses them into a list of dictionaries.

    Args:
        file_path (str): The path to the log file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each representing a parsed
        log line, where each dictionary contains:
            - "date" (str): The date component of the log line.
            - "time" (str): The time component of the log line.
            - "level" (str): The log level component of the log line.
            - "message" (str): The message component of the log line.

    Raises:
        FileNotFoundError: If the file cannot be found.
        RuntimeError: If the file is empty.
        ValueError: If a log line is invalid or cannot be parsed.
    """

    if not Path(file_path).stat().st_size:
        print(f"The file is empty: {file_path}")
        sys.exit(1)

    parsed_logs = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        parsed_log = parse_log_line(line)
                        parsed_logs.append(parsed_log)
                    except ValueError as e:
                        print(f"Skipping line due to error: {e}")
    except FileNotFoundError as exc:
        raise FileNotFoundError('File not found') from exc

    return parsed_logs

if __name__ == "__main__":
    # Example data
    TEST_FILE_PATH = "logs.txt"
    loaded_logs = load_logs(TEST_FILE_PATH)
    print(loaded_logs)

    # Test the function
    assert loaded_logs == expected_logs, (
        f"Test failed for load_logs: got {loaded_logs}, expected {expected_logs}"
    )
    print("All tests passed.")
