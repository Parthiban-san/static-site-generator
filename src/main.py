from textnode import TextType, TextNode
from htmlnode import *
from delimiter import *

def main():
    textnode1 = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    htmlnode1 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(split_nodes_delimiter([TextNode("This is text with a `code``block` word", TextType.TEXT)], "`", TextType.CODE))

if __name__ == "__main__":
    main()