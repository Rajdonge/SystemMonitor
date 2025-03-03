Log Monitoring Script

Overview

This script reads a log file, checks for suspicious patterns, and prints alerts if any are found. It scans for specific keywords indicating potential security threats and extracts timestamps from the log entries.

Features

Detects suspicious log entries such as failed login attempts, unauthorized access, and malicious activity.

Extracts timestamps from log entries if available.

Displays alerts with the detected issue and the corresponding timestamp.

Handles errors gracefully, including file not found exceptions.

Prerequisites

Python 3.x

Installation

Clone this repository or copy the script to your local machine.

Ensure you have Python installed.

Usage

Prepare a log file (e.g., file1.txt) with log entries in the following format:

YYYY-MM-DD HH:MM:SS Log entry message

Example log file content:

2024-12-22 10:45:00 User John failed login attempt from IP 192.168.1.10
2024-12-22 11:00:15 Unauthorized access detected in database server
2024-12-22 12:15:30 Malicious activity detected: Suspicious script execution

Run the script:

python log_monitor.py

Expected Output

If any suspicious activity is detected, the script prints alerts like this:

ALERT: failed login DETECTED AT 2024-12-22 10:45:00
ALERT: unauthorized access DETECTED AT 2024-12-22 11:00:15
ALERT: malicious activity detected DETECTED AT 2024-12-22 12:15:30

Error Handling

If the log file is missing, an error message is displayed:

ERROR: Log file not found at file1.txt

If any other error occurs, the script displays an appropriate error message.

License

This script is provided under the MIT License.

Author

[Your Name]

