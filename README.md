# LSEG_Monitoring_Tool

## Overview
This application reads a CSV log file, tracks job durations, and logs warnings or errors based on processing time thresholds. It is designed to help monitor the performance of scheduled tasks and background jobs.

## Features
- Parses a CSV log file.
- Tracks job start and end times.
- Calculates job durations.
- Logs warnings for jobs exceeding 5 minutes and errors for jobs exceeding 10 minutes.

## Requirements
- Python 3.x
- Standard libraries: `csv`, `datetime`, `logging`, `unittest`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/freeproject999/log-monitoring-app.git
   cd log-monitoring-app
