
def add_module_path():
    import sys
    from pathlib import Path
    module_path = str(Path(__file__).absolute().parent.parent.parent)
    print(module_path)
    if module_path not in sys.path:
        sys.path.append(module_path)
