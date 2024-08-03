"""
Log file processing script.

Reads a log file, counts log levels, and optionally filters logs by a specified log level.
"""

from typing import Dict, List

from load_logs import load_logs
from count_logs_by_level import count_logs_by_level
from display_log_counts import display_log_counts
from print_logs_by_level import print_logs_by_level
from parse_args import parse_arguments

def main() -> None:
    """
    Main function for log file processing. Reads a log file, counts
    log levels, and optionally filters by a specified log level.

    Usage:
        python main.py <logfile_path> [log_level]

    Args:
        None. Command line arguments are used:
            logfile_path (str): Path to the log file.
            log_level (Optional[str]): Optional log level to filter logs (e.g., INFO, ERROR).

    Raises:
        SystemExit: If the log file path is not provided or the file is not found.
    """
    logfile_path, log_level = parse_arguments()

    logs: List[Dict[str, str]] = load_logs(logfile_path)

    log_counts: Dict[str, int] = count_logs_by_level(logs)

    display_log_counts(log_counts, log_level)

    if log_level:
        print_logs_by_level(logs, log_level)

if __name__ == "__main__":
    main()
