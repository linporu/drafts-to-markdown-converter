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
    

def format_ts_YYMMDD(timestamp):
    """Convert ISO format timestamp to YYMMDD format
    
    Args:
        ts (str): ISO format timestamp string, e.g. '1234-11-02T22:56:59Z'
        
    Returns:
        str: YYMMDD format string, e.g. '341102'
        
    Example:
        >>> clean_ts_YYMMDD('1234-11-02T22:56:59Z')
        '341102'
    """
    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return dt.strftime("%y%m%d")