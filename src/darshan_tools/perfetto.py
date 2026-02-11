import json
from typing import List, Dict
import re
import argparse
import pandas as pd


def to_json(data: pd.DataFrame) -> json:
    """ Parse lines from a DXT log file one by one and converts to a trace event json object
    
    Args:
        lines (list): List of lines from a DXT log file.
    Returns:
        trace (Dict): Dictionary containing trace event JSON objects
    """

    trace = {
        "traceEvents": [],
        "displayTimeUnit": "ms"  # Assuming the time unit is milliseconds
    }
    
    for _, row in data.iterrows():
        event_type = row['event_type']
        timestamp = row['time']
        operation = row['operation']
        size = row['size']
        offset = row['offset']
        pid = row['rank']
        duration = row['duration']

        trace_event = {
            "name": f"{event_type}_{operation}",
            "cat" : event_type,
            "ph" : "X",
            "pid": pid,
            "tid": pid,  # Assuming thread ID is same as process ID
            "ts": timestamp * 1000,  # Convert to microseconds
            "dur": duration * 1000,  # Convert to microseconds
            "args": {
                "size": size,
                "offset": offset
            }
        }

        trace["traceEvents"].append(trace_event)
    
    
    return trace
