import os

def generate_file_tree(dir_path, indent='', is_last=True):
    """
    Generate a visually appealing file tree of the specified directory and its subdirectories and files.
    
    Args:
    - dir_path (str): The path of the directory to generate the file tree for.
    - indent (str): The indentation string to use for visual representation.
    - is_last (bool): True if the directory is the last one in the parent directory.
    """
    if not os.path.isdir(dir_path):
        print("Invalid directory path")
        return

    files = os.listdir(dir_path)
    num_files = len(files)

    for i, item in enumerate(sorted(files)):
        item_path = os.path.join(dir_path, item)
        is_directory = os.path.isdir(item_path)
        is_last_item = (i == num_files - 1)
        branch = '└── ' if is_last_item else '├── '

        if is_directory:
            print(indent + branch + '\033[1;34m' + '📁 ' + '\033[0m' + '\033[1;36m' + os.path.basename(item_path) + '/' + '\033[0m')
            next_indent = indent + ('    ' if is_last_item else '│   ')
            generate_file_tree(item_path, next_indent, is_last_item)
        else:
            file_size = os.path.getsize(item_path)
            modified_time = os.path.getmtime(item_path)
            formatted_size = '\033[1;33m' + format_size(file_size) + '\033[0m'
            formatted_modified_time = '\033[1;35m' + format_modified_time(modified_time) + '\033[0m'
            print(indent + branch + '\033[0;32m' + '📄 ' + item + f' (Size: {formatted_size}, Last Modified: {formatted_modified_time})' + '\033[0m')

def format_size(size):
    """
    Format file size to human-readable format.
    
    Args:
    - size (int): File size in bytes.
    
    Returns:
    - str: Formatted file size.
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(suffixes) - 1:
        size /= 1024
        index += 1
    return f'{size:.2f} {suffixes[index]}'

def format_modified_time(timestamp):
    """
    Format timestamp to human-readable date and time.
    
    Args:
    - timestamp (float): Timestamp in seconds since the epoch.
    
    Returns:
    - str: Formatted date and time.
    """
    import datetime
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    current_dir = os.getcwd()
    print("\033[1;35mFile Tree:\033[0m")
    generate_file_tree(current_dir)
