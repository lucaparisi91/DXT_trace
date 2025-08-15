import pytest 
from darshan_tools.perfetto import parse_dxt_lines 
import os 
import json

def test_parse_dxt_lines():

    test_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(test_dir, "example_trace.txt"), "r") as f:
        lines = f.readlines()
        trace = parse_dxt_lines(lines)
        
        assert len(trace["traceEvents"]) == 12
        assert trace["traceEvents"][0]["name"] == "POSIX_read"
        assert trace["traceEvents"][-1]["args"]["size"] == 512
        assert trace["traceEvents"][-1]["args"]["offset"] == 462455872
        