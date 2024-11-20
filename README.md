# Snapshot
## Description

Snapshot is a python app to monitor your system/server. 
It's a tool that creates snapshots of the system’s state, at regular intervals that you can configure (default to 20 in total, every 30 seconds), and outputs to a json-file and the console.

## Motivation

This project is a solution presented to the shapshot-util problem, in the EPAM practice-lab for python

##  How to Install

pip install -U ./snapshot-util

## Usage

snapshot -i 1 -f output.json -n 20

- -i: Interval between snapshots in seconds (type:int, default: 30).
- -f: Output file name (type:str, default: snapshot.json).
- -n: Number of snapshots to output (type:int, default: 20).

All the flags are optional
