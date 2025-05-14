import unittest

from textnode import TextNode, TextType
from text_to_html import (
    text_node_to_html_node,
    extract_markdown_images,
    extract_markdown_links,
    extract_title,
)


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_whitespace(self):
        self.assertEqual(
            extract_title("   #    Welcome to the Jungle   "), "Welcome to the Jungle"
        )

    def test_multiple_headers(self):
        md = "# First Title\n## Subtitle\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")

    def test_no_h1_raises(self):
        with self.assertRaises(ValueError):
            extract_title("## No main header\nJust text")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_comment_line_before_title(self):
        md = "<!-- comment -->\n# Title"
        self.assertEqual(extract_title(md), "Title")


if __name__ == "__main__":
    unittest.main()
