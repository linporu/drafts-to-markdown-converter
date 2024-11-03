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


def format_ts_datetime(timestamp):
    """Convert ISO format timestamp to datetime format
    
    Args:
        timestamp (str): ISO format timestamp string, e.g. '2024-09-20T14:21:59Z'
        
    Returns:
        str: datetime format string, e.g. '2024-09-20 14:21'
        
    Example:
        >>> format_ts_datetime('2024-09-20T14:21:59Z')
        '2024-09-20 14:21'
    """
    dt = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return dt.strftime("%Y-%m-%d %H:%M")


def format_content(timestamp, content):
    """Format content with metadata
    
    Args:
        timestamp: datetime object
        content: original content string
    
    Returns:
        str: formatted content with metadata
    """
    metadata = f"""---
date: {format_ts_datetime(timestamp)}
aliases:
---
Note Type:: #LiteratureNote 
Source Type:: 
Source URL:: 
Author:: 
Topics:: 
Parent note:: 
Sibling note:: 
Child note:: 

---

"""
    content = content.strip()
    return metadata + content