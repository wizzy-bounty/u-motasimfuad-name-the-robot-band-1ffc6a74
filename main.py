import os

ENTRY_TEXT = 'The Low Battery Boys — hit: "Five Percent and Falling in Love"'


def get_output_path():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def main():
    with open(get_output_path(), "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
