import unittest
from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_node_tag(self):
        node1 = HTMLNode("h1")
        self.assertEqual(node1.value,None)
        self.assertEqual(node1.children,None)
        self.assertEqual(node1.props,None)
        self.assertIsNotNone(node1.tag)

    def test_node_value(self):
        node1 = HTMLNode(value="sample text")
        self.assertEqual(node1.tag,None)
        self.assertEqual(node1.children,None)
        self.assertEqual(node1.props,None)
        self.assertIsNotNone(node1.value)

    def test_node_props(self):
        node1 = HTMLNode(props={"href":"www.google.com", "target": "Google"})
        self.assertEqual(node1.tag,None)
        self.assertEqual(node1.children,None)
        self.assertEqual(node1.value,None)
        self.assertIsNotNone(node1.props)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_heading(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_props(self):
        node = LeafNode('a', "Hello, world!", None, {"href":"www.google.com", "target": "Google"})
        self.assertEqual(node.to_html(), f"""<a href="www.google.com" target="Google" >Hello, world!</a>""")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )