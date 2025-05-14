from textnode import TextNode, TextType

import shutil
import os


def main():
    source_dir = "static"
    destination_dir = "public"

    clear_directory(destination_dir)
    copy_recursive(source_dir, destination_dir)


def clear_directory(path):
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


def copy_recursive(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            print(f"Entering directory: {s}")
            copy_recursive(s, d)
        else:
            shutil.copy2(s, d)
            print(f"Copied file: {s} -> {d}")


# Usage
main()
