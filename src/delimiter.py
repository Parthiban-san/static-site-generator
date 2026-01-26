from textnode import *
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        image_list = extract_markdown_images(node.text)
        if len(image_list) == 0:
            new_nodes.append(node)
        else:
            new_node_text = node.text.split(f"![{image_list[0][0]}]({image_list[0][1]})", 1)
            if len(new_node_text[0]) != 0:
                new_nodes.append(TextNode(new_node_text[0], TextType.TEXT, None))
            new_nodes.append(TextNode(image_list[0][0], TextType.IMAGE, image_list[0][1]))
            if len(new_node_text[1]) > 0:
                new_nodes.extend(split_nodes_image([TextNode(new_node_text[1], TextType.TEXT,)]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        link_list = extract_markdown_links(node.text)
        if len(link_list) == 0:
            new_nodes.append(node)
        else:
            new_node_text = node.text.split(f"[{link_list[0][0]}]({link_list[0][1]})", 1)
            if len(new_node_text[0]) != 0:
                new_nodes.append(TextNode(new_node_text[0], TextType.TEXT, None))
            new_nodes.append(TextNode(link_list[0][0], TextType.LINK, link_list[0][1]))
            if len(new_node_text[1]) > 0:
                new_nodes.extend(split_nodes_link([TextNode(new_node_text[1], TextType.TEXT,)]))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def text_to_textnodes(text):
    original_node = [TextNode(text, TextType.TEXT,)]
    bold_nodes = split_nodes_delimiter(original_node, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)
    return link_nodes

def markdown_to_blocks(markdown):
    md_lines = markdown.split("\n\n")
    md_lines_new = [x.strip() for x in md_lines if x != '']
    return md_lines_new

def block_to_block_type(mardown):
    heading = re.findall(r"^#{1,6}\s.*", mardown)
    code = re.findall(r"^```\n([\s\S]*?)```(?<=$)", mardown)
    quote = re.findall(r"^>{1}\s.*", mardown)
    u_list = re.findall(r"^-{1}\s.*", mardown)
    o_list = re.findall(r"^[1-9].\s.*", mardown)
    if len(heading) != 0:
        return BlockType.HEADING
    elif len(code) != 0:
        return BlockType.CODE
    elif len(quote) != 0:
        return BlockType.QUOTE
    elif len(u_list) != 0:
        return BlockType.UNORDERED_LIST
    elif len(o_list) != 0:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH