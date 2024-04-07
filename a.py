import os

def generate_file_tree(dir_path, indent='', is_last=True):
    """
    Generate a file tree of the specified directory and its subdirectories and files.
    
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
            print(indent + branch + os.path.basename(item_path) + '/')
            next_indent = indent + ('    ' if is_last_item else '│   ')
            generate_file_tree(item_path, next_indent, is_last_item)
        else:
            print(indent + branch + item)

if __name__ == "__main__":
    current_dir = os.getcwd()
    print("File Tree:")
    generate_file_tree(current_dir)
