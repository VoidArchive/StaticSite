from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        if text.count(delimiter) % 2 != 0:
            raise ValueError(f"Invalid markdown: Unmatched delimiter {delimiter}")

        parts = []
        remaining_text = text

        while delimiter in remaining_text:
            before, remaining = remaining_text.split(delimiter, 1)
            if before:
                parts.append((before, TextType.TEXT))

            content, remaining_text = remaining.split(delimiter, 1)
            if content:
                parts.append((content, text_type))

        if remaining_text:
            parts.append((remaining_text, TextType.TEXT))

        for content, type in parts:
            new_nodes.append(TextNode(content, type))

    return new_nodes


node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

print(new_nodes)
