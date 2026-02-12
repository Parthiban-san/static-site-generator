from textnode import TextType, TextNode
from htmlnode import *
from delimiter import *
from markdown_converter import *
import os, shutil, sys

def copy_static_to_docs():
    source_path = "./static"
    dest_path = "./docs"
    if os.path.exists(dest_path):
        delete_files(dest_path)
    else:
        os.mkdir(dest_path)
    copy_files(source_path, dest_path)

def copy_files(src, dest):
    for item in os.listdir(src):
        src_item_path = os.path.join(src, item)
        if os.path.isfile(src_item_path) or os.path.islink(src_item_path):
            shutil.copy(src_item_path, dest)
            print(f"{item} file copied to {dest}.")
        elif os.path.isdir(src_item_path):
            dest_item_path = os.path.join(dest, item)
            os.mkdir(dest_item_path)
            print(f"{dest_item_path} folder created.")
            copy_files(src_item_path, dest_item_path) 

def delete_files(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
            print(f"{item_path} file deleted.")
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"{item_path} folder deleted.")

def extract_title(markdown):
    with open(markdown, 'r') as file:
        md_title = re.findall(r'^#{1}\s.*', file.read())
        if len(md_title) == 0:
            raise Exception("No heading present in markdown file.")
        html_title = md_title[0].split(" ", 1)[1]
    return html_title.strip()

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as md_file:
        md_content = md_file.read()
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    md_html = markdown_to_html_node(md_content).to_html()
    html_title = extract_title(from_path)
    final_html = template_content.replace(r"{{ Title }}", html_title)
    final_html = final_html.replace(r"{{ Content }}", md_html)
    final_html = final_html.replace(f"href=\"/", f"href=\"{base_path}")
    final_html = final_html.replace(f"src=\"/", f"src=\"{base_path}")
    with open(dest_path, "w") as dest_file:
        dest_file.write(final_html)

def generate_pages_recursive(base_path, from_path = "content", dest_path = "docs"):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    for item in os.listdir(from_path):
        item_path = os.path.join(from_path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            generate_page(item_path, "template.html", os.path.join(dest_path, "index.html"), base_path)
        elif os.path.isdir(item_path):
            generate_pages_recursive(base_path, item_path, item_path.replace("content", "docs"))

    pass

def main(base_path):
    copy_static_to_docs()
    generate_pages_recursive(base_path)

if __name__ == "__main__":
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    main(basepath)