import re  # Importing "re" module to use regular expressions

def monitor_logs(log_file_path):

    """
    Reads a log file, checks for suspicious patterns, and prints alerts if any are found.
    
    :param log_file_path: Path to the log file.
    """

    # List of suspicious patterns that indicate malicious activity
    suspicious_patterns = [
        r"failed login",
        r"unauthorized access",
        r"malicious activity detected",
    ]

    # Regular expression pattern to detect timestamps in the format YYYY-MM-DD HH:MM:SS
    timestamp_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    try:
        # Open the log file for reading
        with open(log_file_path, "r") as log_file:
            # Read each suspicious pattern in the log line
            for line in log_file:
                for pattern in suspicious_patterns:
                    if re.search(pattern, line, re.IGNORECASE): # Case insensitive search

                        # Extract the timestamp if available
                        timestamp_match = timestamp_pattern.search(line)
                        # If timestamp is found, extract it, otherwise set it to "N/A"
                        timestamp = timestamp_match.group(0) if timestamp_match else "N/A"

                        print(f"AlERT: {pattern} DETECTED AT {timestamp}")
    
    except FileNotFoundError:
        # Handle the case where the log file is not found
        print(f"ERROR: Log file not found at {log_file_path}")
        
    except Exception as e:
        # Handle any other unexpected errors
        print(f"ERROR: An error occurred - {str(e)}")


# Usage
log_file = "file1.txt"  # Path to the log file
monitor_logs(log_file)  # Call the function with the log file path