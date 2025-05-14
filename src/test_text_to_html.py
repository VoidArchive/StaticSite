import unittest

from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node


def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")


def test_bold(self):
    node = TextNode("Bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "Bold text")
    self.assertEqual(html_node.props, {})


def test_italic(self):
    node = TextNode("Italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "Italic text")
    self.assertEqual(html_node.props, {})


def test_code(self):
    node = TextNode("Code snippet", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "Code snippet")
    self.assertEqual(html_node.props, {})


def test_link(self):
    node = TextNode("Click here", TextType.LINK, "https://example.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "Click here")
    self.assertEqual(html_node.props, {"href": "https://example.com"})


def test_image(self):
    node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "Alt text"})


if __name__ == "__main__":
    unittest.main()
