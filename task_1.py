import os
import shutil
import argparse


def copy_and_sort_files(src_dir, dest_dir):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_and_sort_files(src_path, dest_dir)
            elif os.path.isfile(src_path):
                file_ext = os.path.splitext(item)[1][1:]

                if not file_ext:
                    file_ext = "no_extension"

                ext_dir = os.path.join(dest_dir, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                shutil.copy2(src_path, os.path.join(ext_dir, item))
                print(f"Copied {src_path} to {os.path.join(ext_dir, item)}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("src_dir", help="Source directory")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Destination directory (default: dist)")
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if dest_dir == "dist":
        dest_dir = os.path.join(os.getcwd(), dest_dir)

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    if not os.path.exists(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist. Creating directory...")
        os.makedirs(dest_dir)

    copy_and_sort_files(src_dir, dest_dir)
    print("File copy and sorting completed.")


if __name__ == "__main__":
    main()
