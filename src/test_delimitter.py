import unittest
from textnode import TextType, TextNode
from htmlnode import *
from delimiter import *

class TestDelimitter(unittest.TestCase):
    def test_eq(self):
        split_nodes = split_nodes_delimiter([TextNode("This is text with a `code``block` word", TextType.TEXT)], "`", TextType.CODE)
        nodes_list = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code", TextType.CODE, None), TextNode("block", TextType.CODE, None), TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(split_nodes, nodes_list)

    def test_not_eq(self):
        split_nodes = split_nodes_delimiter([TextNode("This is text with a `code``block` word", TextType.TEXT)], "`", TextType.CODE)
        nodes_list = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code", TextType.TEXT, None), TextNode("block", TextType.CODE, None), TextNode(" word", TextType.TEXT, None)]
        self.assertNotEqual(split_nodes, nodes_list)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("link", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes_list = text_to_textnodes("""This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)""")
        expected_nodes = [TextNode("This is ", TextType.TEXT, None), TextNode("text", TextType.BOLD, None), TextNode(" with an ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None), TextNode(" word and a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), TextNode(" and an ", TextType.TEXT, None), TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT, None), TextNode("link", TextType.LINK, "https://boot.dev")]
        self.assertListEqual(nodes_list, expected_nodes)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("Test subject"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("- Test subject"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Test subject"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("> Test subject"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("""```\n Test subject\n```"""), BlockType.CODE)
        self.assertEqual(block_to_block_type("""# Heading"""), BlockType.HEADING)