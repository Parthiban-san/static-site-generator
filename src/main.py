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
    print(split_nodes_link([TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png) and [image](https://i.imgur.com/zjjcJKZ.png)",
        TextType.TEXT,
    )]))

if __name__ == "__main__":
    main()