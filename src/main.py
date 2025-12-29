from textnode import TextType, TextNode
from htmlnode import *

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
    print(htmlnode1.to_html())

if __name__ == "__main__":
    main()