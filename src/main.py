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
    print(text_to_textnodes("""This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"""))

if __name__ == "__main__":
    main()