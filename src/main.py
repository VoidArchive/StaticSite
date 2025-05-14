from text_to_html import extract_title
from blocktype import markdown_to_html_node
import shutil
import os
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    source_dir = "static"
    destination_dir = "docs"
    template_path = "template.html"

    clear_directory(destination_dir)
    copy_recursive(source_dir, destination_dir)

    generate_pages_recursive("content", template_path, destination_dir, basepath)


def generate_pages_recursive(content_dir, template_path, dest_dir, basepath):
    for root, dirs, files in os.walk(content_dir):
        rel_path = os.path.relpath(root, content_dir)

        if rel_path != ".":
            output_dir = os.path.join(dest_dir, rel_path)
        else:
            output_dir = dest_dir

        os.makedirs(output_dir, exist_ok=True)

        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(root, file)

                if file == "index.md":
                    html_file_path = os.path.join(output_dir, "index.html")
                else:
                    html_file_name = os.path.splitext(file)[0] + ".html"
                    html_file_path = os.path.join(output_dir, html_file_name)

                generate_page(md_file_path, template_path, html_file_path, basepath)


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


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    filled_content = template_content.replace("{{ Title }}", title)
    filled_content = filled_content.replace("{{ Content }}", html_content)

    filled_content = filled_content.replace('href="/', f'href="{basepath}')
    filled_content = filled_content.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(filled_content)


main()
