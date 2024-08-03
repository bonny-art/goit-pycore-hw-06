"""
Handles command-line argument parsing for log file processing.
"""

import sys
from typing import Optional, Tuple
from pathlib import Path

def parse_arguments() -> Tuple[str, Optional[str]]:
    """
    Parses command-line arguments.

    Returns:
        Tuple[str, Optional[str]]: A tuple containing the log file path and an optional log level.
    
    Raises:
        SystemExit: If the log file path is not provided or the file is not found.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile_path> [log_level]")
        sys.exit(1)

    logfile_path: str = sys.argv[1]
    log_level: Optional[str] = sys.argv[2].upper() if len(sys.argv) > 2 else None

    if not Path(logfile_path).is_file():
        print(f"File not found: {logfile_path}")
        sys.exit(1)

    return logfile_path, log_level
