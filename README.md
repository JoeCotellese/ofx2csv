# ofx2csv
Python script that converts .ofx and .qfx files to .csv

# Installing

This project relies on Poetry being installed on your system.

```bash
    poetry install
```

# Running
1. Put the ofx files in the same folder as `ofx2csv.py`
2. Do 

    ```bash
    python ofx2csv.py
    ```

# Options

## JSON Output

It defaults to `csv`. You can also request JSON.

```bash
python ofx2csv.py -o json
```

## Specify a file

It defaults to `*.ofx`; you can specify a file if you want:

```bash
python ofx2csv.py -i foo.qfx
```

Or two files:

```bash
python ofx2csv.py -i foo.qfx bar.qfx
```

You can also include wildcards:

```bash
python ofx2csv.py -i 2024-*.qfx bar.qfx
```
