import os

def cleanup_files(*file_paths):
    """
    Removes the specified files if they exist.
    """
    for path in file_paths:
        if os.path.exists(path):
            try:
                os.remove(path)
            except Exception as e:
                print(f"Error removing file {path}: {e}")
