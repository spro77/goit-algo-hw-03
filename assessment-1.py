import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dest_dir):
    try:
        items = os.listdir(src_dir)
    except Exception as e:
        print(f"Error accessing source directory {src_dir}: {e}")
        return

    for item in items:
        src_path = os.path.join(src_dir, item)

        if os.path.isfile(src_path):
            ext = os.path.splitext(item)[1][1:].lower() or 'no_ext'
            target_dir = os.path.join(dest_dir, ext)
            try:
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy2(src_path, os.path.join(target_dir, item))
            except Exception as e:
                print(f"Error copying file {src_path} to {target_dir}: {e}")
        elif os.path.isdir(src_path):
            copy_and_sort_files(src_path, dest_dir)


def main():
    parser = argparse.ArgumentParser(description="Copy and Sort Files")
    parser.add_argument('src', help='Source directory')
    parser.add_argument('dest', nargs='?', default='dist', help='Destination directory (default: dist)')
    args = parser.parse_args()

    if not os.path.isdir(args.src):
        print(f"Source directory does not exist: {args.src}")
        return

    os.makedirs(args.dest, exist_ok=True)
    copy_and_sort_files(args.src, args.dest)

if __name__ == '__main__':
    main()