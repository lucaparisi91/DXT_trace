""" DXT to Perfetto Trace Converter

This script converts a DXT trace in text format to a json object and prints it to stndard output. 
The json file can be visualized using the Perfetto UI.

"""

import argparse
from darshan_tools.perfetto import parse_dxt_lines
import json


if __name__== "__main__":

    parser = argparse.ArgumentParser(description="Convert DXT trace to Perfetto trace format.")
    parser.add_argument("input_file", help="Path to the DXT trace in text format.")
    args = parser.parse_args()
    
    with open(args.input_file, "r") as f:
        lines = f.readlines()
        trace = parse_dxt_lines(lines)
        print(json.dumps(trace, indent=2))