""" DXT to Perfetto Trace Converter

This script converts a DXT trace in text format to a json object and prints it to stndard output. 
The json file can be visualized using the Perfetto UI.

"""

import argparse
from darshan_tools.perfetto import to_json
from darshan_tools.parser import parse_dxt
import json


if __name__== "__main__":

    parser = argparse.ArgumentParser(description="Convert DXT trace to Perfetto trace format.")
    parser.add_argument("input_file", help="Path to the DXT trace in text format.")
    args = parser.parse_args()

    df = parse_dxt(args.input_file)
    trace = to_json(df)
    print(json.dumps(trace, indent=2))