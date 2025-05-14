import unittest

from blocktype import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockType(unittest.TestCase):
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

    def test_paragraph(self):
        block = "This is a simple paragraph with no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        block = "This is a multi-line paragraph\nwith no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# Heading level 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "## Heading level 2"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        block = "###### Heading level 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

        # Should be a paragraph, not a heading
        block = "####### Too many #"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        # Should be a paragraph, no space after #
        block = "#NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = "```python\ndef hello():\n    print('Hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        # Should be a paragraph, not a code block
        block = "```code block without closing"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
