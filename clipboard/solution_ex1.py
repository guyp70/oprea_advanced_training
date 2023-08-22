import pyperclip


def main():
    # Get the text from the clipboard
    text = pyperclip.paste()
    print(f"Text from clipboard: {text}")


if __name__ == "__main__":
    main()
