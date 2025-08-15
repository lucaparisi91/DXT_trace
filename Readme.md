# Convert a DXT trace to a Perfetto trace

This script converts a DXT trace to a Perfetto trace.
You can convert a trace generate with `darshan-dxt-parser` to a json trace for visualisation, as the in the example below

```bash
python3 bin/dxt-to-perfetto.py dxt-trace.txt > trace.json
```

You can run tests with 

```bash
pytest -vvv --capture=tee-sys tests
```

Json generated is baed on the perfetto JSON format described at
https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview?tab=t.0 .
