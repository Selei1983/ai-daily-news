#!/usr/bin/env python3
"""Check which python packages are available."""
import importlib
for m in ["requests", "markdown", "bs4", "PIL", "yaml"]:
    try:
        importlib.import_module(m)
        print(f"{m}: OK")
    except Exception as e:
        print(f"{m}: MISSING ({e.__class__.__name__})")
