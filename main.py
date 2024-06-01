#!/usr/bin/env python
"""Utility for creating python projects via the command line in Windows"""

from PowershellHandler import run
from Parser import namespace

if __name__ == "__main__":
    parsed = namespace()  # Get args

    project_name: str = parsed.name  # Stores project name from args
    version: str = ""

    if parsed.version:
        version = parsed.version

    run(f"mkdir {project_name}")  # Create directory with project name
