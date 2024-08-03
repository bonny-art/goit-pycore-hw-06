"""
Test data for log processing functions.

Includes:
- log_lines: Sample log lines as strings.
- loaded_logs: Parsed log data as dictionaries.
- expected_filtered_logs: Expected results for filtered logs by INFO level.
- expected_counts: Expected counts of log levels.
"""

log_lines = [
    "2024-01-22 08:30:01 INFO User logged in successfully.",
    "2024-01-22 08:45:23 DEBUG Attempting to connect to the database.",
    "2024-01-22 09:00:45 ERROR Database connection failed.",
    "2024-01-22 09:15:10 INFO Data export completed.",
    "2024-01-22 10:30:55 WARNING Disk usage above 80%.",
    "2024-01-22 11:05:00 DEBUG Starting data backup process.",
    "2024-01-22 11:30:15 ERROR Backup process failed.",
    "2024-01-22 12:00:00 INFO User logged out.",
    "2024-01-22 12:45:05 DEBUG Checking system health.",
    "2024-01-22 13:30:30 INFO Scheduled maintenance."
]

loaded_logs = [
    {
        "date": "2024-01-22",
        "time": "08:30:01",
        "level": "INFO",
        "message": "User logged in successfully."
    },
    {
        "date": "2024-01-22",
        "time": "08:45:23",
        "level": "DEBUG",
        "message": "Attempting to connect to the database."
    },
    {
        "date": "2024-01-22",
        "time": "09:00:45",
        "level": "ERROR",
        "message": "Database connection failed."
    },
    {
        "date": "2024-01-22",
        "time": "09:15:10",
        "level": "INFO",
        "message": "Data export completed."
    },
    {
        "date": "2024-01-22",
        "time": "10:30:55",
        "level": "WARNING",
        "message": "Disk usage above 80%."
    },
    {
        "date": "2024-01-22",
        "time": "11:05:00",
        "level": "DEBUG",
        "message": "Starting data backup process."
    },
    {
        "date": "2024-01-22",
        "time": "11:30:15",
        "level": "ERROR",
        "message": "Backup process failed."
    },
    {
        "date": "2024-01-22",
        "time": "12:00:00",
        "level": "INFO",
        "message": "User logged out."
    },
    {
        "date": "2024-01-22",
        "time": "12:45:05",
        "level": "DEBUG",
        "message": "Checking system health."
    },
    {
        "date": "2024-01-22",
        "time": "13:30:30",
        "level": "INFO",
        "message": "Scheduled maintenance."
    }
]

expected_filtered_logs = [
    {
        "date": "2024-01-22",
        "time": "08:30:01",
        "level": "INFO",
        "message": "User logged in successfully."
    },
    {
        "date": "2024-01-22",
        "time": "09:15:10",
        "level": "INFO",
        "message": "Data export completed."
    },
    {
        "date": "2024-01-22",
        "time": "12:00:00",
        "level": "INFO",
        "message": "User logged out."
    },
    {
        "date": "2024-01-22",
        "time": "13:30:30",
        "level": "INFO",
        "message": "Scheduled maintenance."
    }
]

expected_counts = {
        'INFO': 4,
        'DEBUG': 3,
        'ERROR': 2,
        'WARNING': 1
    }

LOG_SELECTED = "INFO"
