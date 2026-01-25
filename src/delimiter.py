from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            current_node_texts = node.text.split(delimiter)
            for i in range(len(current_node_texts)):
                if len(current_node_texts[i]) != 0:
                    if i%2 == 0:
                        new_nodes.append(TextNode(current_node_texts[i],TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(current_node_texts[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)