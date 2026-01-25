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