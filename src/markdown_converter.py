from delimiter import *
from htmlnode import *
from textnode import *

def markdown_to_html_node(markdown):
    md_list = markdown_to_blocks(markdown)
    children = []
    for md_block in md_list:
        md_type = block_to_block_type(md_block)
        match md_type:
            case BlockType.HEADING:
                children.append(heading_to_html_node(md_block))
            case BlockType.CODE:
                children.append(code_to_html_node(md_block))
            case BlockType.QUOTE:
                children.append(quote_to_html_node(md_block))
            case BlockType.UNORDERED_LIST:
                children.append(list_to_html_node(md_block, BlockType.UNORDERED_LIST))
            case BlockType.ORDERED_LIST:
                children.append(list_to_html_node(md_block, BlockType.ORDERED_LIST))
            case _:
                children.append(paragraph_to_html_node(md_block))
    return ParentNode("div", children)

def heading_to_html_node(block):
    heading_len = block.split(" ", 1)
    return ParentNode(f"h{len(heading_len[0])}", text_to_children_quote(heading_len[1]))

def code_to_html_node(block):
    list_items = list(filter(lambda x : ((x!="")), block.split("`")))
    return ParentNode("pre", [LeafNode("code", list_items[0].lstrip("\n"))])

def quote_to_html_node(block):
    return ParentNode("blockquote", text_to_children_quote(block))

def paragraph_to_html_node(block):
    return ParentNode("p", text_to_children(block))

def list_to_html_node(block, list_type):
    list_items = [x for x in block.split("\n") if x!='']
    tag = ''
    if list_type == BlockType.UNORDERED_LIST:
        tag = "ul"
    elif list_type == BlockType.ORDERED_LIST:
        tag = "ol"
    parentNode = ParentNode(tag, [])
    for li in list_items:
        if list_type == BlockType.UNORDERED_LIST:
            li = li.split("- ", 1)[1]
        elif list_type == BlockType.ORDERED_LIST:
            li = li.split(" ", 1)[1]
        parentNode.children.append(ParentNode("li", text_to_children(li)))
    return parentNode


def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for t_node in text_nodes:
        html_nodes.append(text_node_to_html_node(t_node))
    return html_nodes

def text_to_children_quote(block):
    block = block.replace("> ", "").replace(">\n","\n")
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for t_node in text_nodes:
        html_nodes.append(text_node_to_html_node(t_node))
    return html_nodes



        
            