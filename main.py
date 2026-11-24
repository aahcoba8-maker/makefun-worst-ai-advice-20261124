import os

LINE = "Certainly! Deleting System32 frees up gigabytes \u2014 Windows keeps it around just in case, but honestly, you won't miss it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir or not os.path.isdir(out_dir):
        if os.path.isdir("/output"):
            out_dir = "/output"
        else:
            out_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
