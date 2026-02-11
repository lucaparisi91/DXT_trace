# darshan_tools

This package contains some tools for the analysis of darshan parsed outputs.


## Installing

You can install with pip using

```bash
pip install -e .
```

## Usage

### DXT trace to perfetto

A darshan DXT trace can be converted to a json file using the `dxt-to-perfetto dxt-trace.txt` command, where  `dxt-trace.txt` is the name of a file containing output from the darshan-util tool `darshan-dxt-parser` . For example , one my use

```bash
darshan-dxt-parser my_profile.darshan > dxt-trace.txt
dxt-to-perfetto dxt-trace.txt > trace.json
```

The generated JSON output is based on the perfetto JSON format described at
https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview?tab=t.0 .

## Testing

You can run tests with 

```bash
pytest -vvv --capture=tee-sys src/tests
```

