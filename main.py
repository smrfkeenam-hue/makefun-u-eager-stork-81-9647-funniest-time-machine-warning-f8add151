import os

ENTRY = "CAUTION: If you meet yourself, do not say hello. You already know how this ends."


def write_entry(text, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    write_entry(ENTRY, entry_path())


if __name__ == "__main__":
    main()
