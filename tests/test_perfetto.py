import pytest 
from darshan_tools.perfetto import to_json
from darshan_tools.parser import parse_dxt
import os 
import json

def test_to_json():
    """ Test converting a dataframe to JSON trace format for perfetto. """

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, "example_trace.txt")
    
    df = parse_dxt(test_file)

    trace = to_json(df)

    assert len(trace["traceEvents"]) == 12
    assert trace["traceEvents"][0]["name"] == "POSIX_read"
    assert trace["traceEvents"][-1]["args"]["size"] == 512
    assert trace["traceEvents"][-1]["args"]["offset"] == 462455872
    