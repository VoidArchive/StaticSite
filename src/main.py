from textnode import TextNode, TextType


def main():
    a = TextNode("hello", TextType.LINK, "https://anish.dev")
    print(a)


main()
