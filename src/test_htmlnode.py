import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(
            tag="a",
            value="Click me",
            children=None,
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_with_no_props(self):
        # Test with no properties
        node = HTMLNode(tag="p", value="Hello", children=None, props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr_method(self):
        # Test the __repr__ method
        node = HTMLNode(
            tag="div",
            value=None,
            children=[HTMLNode(tag="p", value="Paragraph", children=None, props={})],
            props={"class": "container"},
        )
        expected = "HTMLNode(tag=div, value=None, children=[HTMLNode(tag=p, value=Paragraph, children=None, props={})], props={'class': 'container'})"
        self.assertEqual(repr(node), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

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

    def test_parentnode_renders_children(self):
        parent = ParentNode("div", [LeafNode("span", "child text")])
        self.assertEqual(parent.to_html(), "<div><span>child text</span></div>")

    def test_parentnode_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "text")]).to_html()


if __name__ == "__main__":
    unittest.main()
