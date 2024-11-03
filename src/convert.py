import json
from helper import *
import sys


def main():
    if len(sys.argv) != 2:
         sys.exit("Usage: python convert.py [filename]")

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        drafts = json.load(f)
        for draft in drafts:
            create_ts = draft["created_at"]
            content = draft["content"]

            # Format
            YYMMDD_ts = format_ts_YYMMDD(create_ts)
            formatted_content = format_content(create_ts, content)
            file_name = f"{YYMMDD_ts}.md"
            
            save(file_name, formatted_content)
            

if __name__ == "__main__":
        main()
