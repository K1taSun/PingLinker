#!/usr/bin/env python3
import sys
import io

# Fix for Windows Unicode support
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding='utf-8')

from pinglinker.cli import cli

if __name__ == '__main__':
    cli()
