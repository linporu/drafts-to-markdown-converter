import datetime


def save(file_name, content):
    """Save content to 'YYMMDD title.md'"""
    try:
        file_path = "output/" + file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Content saved to {file_path}")
        return file_path
    except IOError as e:
        print(f"Error: 「{e}」")
        return None