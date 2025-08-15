""" Darshan Summary and DXT Log Parser

This module provides functions to parse Darshan summary and DXT log files into Pandas DataFrames from their text formats.
"""

import pandas as pd
import re

def parse_summary(filename: str) -> pd.DataFrame:
    """ Parse lines from a Darshan summary log file one by one and converts to a Pandas DataFrame

    Args:
        filename (str): Path to the Darshan summary log file.

    Returns:
        pd.DataFrame: DataFrame containing the parsed Darshan summary log data.
    """

    summary_data = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            pattern = r"\s*(POSIX)\s+(\d+)\s+\d+\s+(\S+)\s+(\d+)\s(\S+)"
            m = re.match(pattern, line)

            if m is not None:
                layer = m.group(1)
                rank = int(m.group(2))
                operation = str(m.group(3))
                value = int(m.group(4))
                filename = str(m.group(5))
                
                event = {
                    "layer": layer,
                    "operation": operation,
                    "rank": rank,
                    "value": value,
                    "filename": filename
                }

                summary_data.append(event)

    df = pd.DataFrame(summary_data)
    return df


def parse_dxt(filename: str) -> pd.DataFrame:

    """ Parse lines from a DXT log file one by one and converts to a Pandas DataFrame

    Args:
        filename (str): Path to the DXT log file.

    Returns:
        pd.DataFrame: DataFrame containing the parsed DXT log data.
    """

    events = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            pattern =r"\s*X_([A-Z]+)\s+(\d+)\s+(read|write)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+(?:\.\d*)?)\s+(\d+(?:\.\d*)?)"
            m=re.match(pattern, line)
            
            if m is not None:
                event_type = m.group(1)
                timestamp = float(m.group(7))
                operation = m.group(3)
                size = int(m.group(6))
                offset = int(m.group(5))
                rank = int(m.group(2))
                duration = float(m.group(8)) - timestamp

                event = {
                    "event_type": event_type,
                    "operation": operation,
                    "rank": rank,
                    "time": timestamp,
                    "duration": duration,
                    "size": size,
                    "offset": offset
                }

                events.append(event)
        
    df = pd.DataFrame(events)
    return df
