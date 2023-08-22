import pyperclip
import os
import hashlib


def get_file_md5sum(file_path: str) -> str:
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def main():

    while True:
        path = pyperclip.waitForNewPaste()
        if os.path.isfile(path):
            md5sum = get_file_md5sum(path)
            pyperclip.copy(md5sum)
            print(f'Calculated md5sum for "{path}": {md5sum}')
        else:
            pyperclip.copy("")
            print(
                f'Clipboard does not contain a valid file path! (path: "{path}")',
            )


if __name__ == "__main__":
    main()
