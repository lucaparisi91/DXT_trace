""" DXT to Perfetto Trace Converter

This script converts a DXT trace in text format to a json object and prints it to stndard output. 
The json file can be visualized using the Perfetto UI.

"""


import json
from typing import List, Dict
import re
import argparse

def parse_dxt_lines(lines: List[str]) -> Dict:
    """ Parse lines from a DXT log file one by one and converts to a trace event json object
    
    Args:
        lines (list): List of lines from a DXT log file.
    Returns:
        trace (Dict): Dictionary containing trace event JSON objects
    """

    trace = {
        "traceEvents": [],
    }

    for line in lines:
        pattern =r"\s*X_([A-Z]+)\s+(\d+)\s+(read|write)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+(?:\.\d*)?)\s+(\d+(?:\.\d*)?)"
        m=re.match(pattern, line)
        
        if m is not None:
            event_type = m.group(1)
            timestamp = float(m.group(7))
            operation = m.group(3)
            size = int(m.group(6))
            offset = int(m.group(5))
            pid = int(m.group(2))
            duration = float(m.group(8)) - timestamp

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

if __name__== "__main__":

    parser = argparse.ArgumentParser(description="Convert DXT trace to Perfetto trace format.")
    parser.add_argument("input_file", help="Path to the DXT trace in text format.")
    args = parser.parse_args()
    
    with open(args.input_file, "r") as f:
        lines = f.readlines()
        trace = parse_dxt_lines(lines)
        print(json.dumps(trace, indent=2))