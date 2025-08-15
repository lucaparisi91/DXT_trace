import pytest 
from darshan_tools.parser import parse_dxt
import os 
import json


def test_parse_dxt():
    """ Test the parse_dxt function with a sample DXT trace file. """

    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_dir, "example_trace.txt")

    df = parse_dxt(test_file)

    assert df.shape[0] == 12
    assert df["event_type"].iloc[0] == "POSIX"
    assert df["operation"].iloc[0] == "read"
    assert df["rank"].iloc[0] == 0
    assert df["size"].iloc[-1] == 512
    assert df["offset"].iloc[-1] == 462455872
