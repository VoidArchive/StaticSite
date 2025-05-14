from textnode import TextNode, TextType
from text_to_html import extract_markdown_images, extract_markdown_links


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


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        extracted_image = extract_markdown_images(text)
        if not extracted_image:
            new_nodes.append(old_node)
            continue

        remaning_text = text
        for alt_text, image_url in extracted_image:
            before, remaning = remaning_text.split(f"![{alt_text}]({image_url})", 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))

            remaning_text = remaning

        if remaning_text:
            new_nodes.append(TextNode(remaning_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        extracted_link = extract_markdown_links(text)
        if not extracted_link:
            new_nodes.append(old_node)
            continue

        remaning_text = text
        for link_text, link_url in extracted_link:
            before, remaning = remaning_text.split(f"[{link_text}]({link_url})", 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            remaning_text = remaning

        if remaning_text:
            new_nodes.append(TextNode(remaning_text, TextType.TEXT))

    return new_nodes
