import sys
import os
from pathlib import Path

# Add the shared_code directory to sys.path
shared_code_dir = str(Path(__file__).resolve().parent.parent / 'shared_code')
if shared_code_dir not in sys.path:
    sys.path.append(shared_code_dir)


