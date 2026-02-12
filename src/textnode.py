from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

def text_node_to_html_node(text_node):
    htmlNode = None
    match text_node.text_type:
        case TextType.TEXT:
            htmlNode = LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            htmlNode = LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            htmlNode = LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            htmlNode = LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            htmlNode = LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            htmlNode = LeafNode(tag="img", value=" ", props={"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Text type does not match any predefined values")
    return htmlNode

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode1):
        if (textnode1.text == self.text) and (textnode1.text_type == self.text_type) and (textnode1.url == self.url):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"