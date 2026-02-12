from textnode import TextType, TextNode
from htmlnode import *
from delimiter import *
from markdown_converter import *
import os, shutil

def copy_static_to_public():
    source_path = "./static"
    dest_path = "./public"
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

def main():
    copy_static_to_public()

if __name__ == "__main__":
    main()