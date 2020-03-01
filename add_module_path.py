import sys
from pathlib import Path
module_path = str(Path(__file__).absolute().parent)
print(module_path)
if module_path not in sys.path:
    sys.path.append(module_path)

