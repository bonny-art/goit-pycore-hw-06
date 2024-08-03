"""
Module for parsing log lines into components.

Includes:
- parse_log_line: Converts a log line into a dictionary of its components.
"""

from typing import Dict

from test_data import log_lines, loaded_logs as expected_results

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parses a single log line into its components.

    Args:
        line (str): A log line in the format "YYYY-MM-DD HH:MM:SS LEVEL Message".

    Returns:
        Dict[str, str]: A dictionary with the parsed components:
            - "date" (str): The date component of the log line.
            - "time" (str): The time component of the log line.
            - "level" (str): The log level component of the log line.
            - "message" (str): The message component of the log line.
    """

    components = line.split(' ', 3)

    if len(components) != 4:
        raise ValueError(f"Line format invalid: {line}")

    return {
        "date": components[0],
        "time": components[1],
        "level": components[2],
        "message": components[3]
    }

if __name__ == "__main__":
    for log_line, expected in zip(log_lines, expected_results):
        # Example data
        parsed_line = parse_log_line(log_line)
        print(parsed_line)

        # Test the function
        assert parsed_line == expected, (
            f"Test failed for line: {log_line}. Expected: {expected}, Got: {parsed_line}"
        )

    print("All tests passed.")
