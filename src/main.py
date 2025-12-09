from textnode import TextType, TextNode

def main():
    textnode1 = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(textnode1)

if __name__ == "__main__":
    main()