import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    print(f"DEBUG: Checking if '{source_dir_path}' exists...")

    if not os.path.exists(source_dir_path):
        print(f"ERROR: Source directory '{source_dir_path}' does not exist. Check the path.")
        return  # Skip instead of crashing

    if not os.path.exists(dest_dir_path):
        print(f"DEBUG: Creating destination directory '{dest_dir_path}'...")
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f"DEBUG: Copying {from_path} -> {dest_path}")

        if os.path.isfile(from_path):
            try:
                shutil.copy(from_path, dest_path)
                print(f"SUCCESS: {from_path} copied to {dest_path}")
            except Exception as e:
                print(f"ERROR: Could not copy {from_path} -> {dest_path}. Exception: {e}")
        else:
            copy_files_recursive(from_path, dest_path)
