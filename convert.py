import json
import sys


def main():
    if len(sys.argv) != 2:
         sys.exit("Usage: python convert.py [filename]")

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        drafts = json.load(f)
        for draft in drafts:
            create_ts = draft["created_at"]
            content = draft["content"]
            print(create_ts, content)


if __name__ == "__main__":
        main()
