# Guild Wars 2 Log Aggregator

## Summary

A tool primarily design for GvG log aggregation to help in reviewing relatively homogenous data from a single session of play. PvE and multi-scrim data is not explicitly supported, but will likely function fairly well so long as the input data is of relatively high quality (low number of player swaps, all same instance and patch). See here for a previous project in the same vein. This project is trying to find a more appropriate user fit by not attempting to target online functionality, and instead prioritising compatibility and ease of distribution.

## How to use

Download the latest release of GW2 Elite Insights parser by Eliphas here: <https://github.com/baaron4/GW2-Elite-Insights-Parser> Grab the latest release of the python executable from this repository Start up the application, and configure your settings by selecting the path to your downloaded Elite Insights Parser, and the input directory where you have a curated selection of zevtc arcdps logs.

> **!Important!** Ideally make a separate directory for each aggregated set of data, as leftover zevtc and json logs from other play sessions may contaminate subsequent application runs if the input directory is not changed.

## Notes

A rework of the initial typescript based tool that had a few too many pivots in design decisions. That initial project may still function for a while but is not being actively maintained as I am now focusing on this python port. <https://github.com/Ariacell/GW2EI-Aggregator>

## Roadmap

- :heavy_check_mark: Basic settings, Elite Insights integration, Steel Thread log aggregation into unique player names
- :heavy_check_mark: Pydantic modelling for the EI data structure
- :hourglass: Improve pyinstaller publishing to prevent false flagging of the executable as a virus for users
- :hourglass: Port existing logic from typescript project
- :hourglass: Enhance UI output with new data structure from pydantic
- :hourglass: Add multithreaded log aggregation support
- :hourglass: Add CSV export options

## Contributing

### Prerequisites

### Setup

Start a venv

```sh
python -m venv venv
```

Activate the venv and install dependencies with

```sh
./venv/Scripts/activate
poetry install
```

### Running the application locally

```sh
poetry run ./pygw2agg/main.py
```

### Building a release

You will need nuitka on your path: <https://nuitka.net/doc/user-manual.html>

```sh
nuitka .\pygw2agg\main.py --follow-imports --standalone --enable-plugin=tk-inter
```

This will create a main.dist folder that can be zipped for release without triggering windows defender or other anti-virus software. An installer could be implemented later on.
