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
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))

if __name__ == "__main__":
    main()