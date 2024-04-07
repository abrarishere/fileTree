
---

# File Tree Generator

## Overview

The File Tree Generator is a Python script designed to create a visual representation of a directory structure, including subdirectories and files. The generator comes in two versions: `a.py` and `a-full.py`, each offering unique features to meet different needs.

### a.py

The `a.py` script generates a basic file tree using ASCII characters. It provides a simple yet effective way to visualize directory structures.

### a-full.py

On the other hand, `a-full.py` is an enhanced version of `a.py` with additional features such as icons, file sizes, last modified dates, and colorization. This version offers a more detailed and visually appealing representation of directory structures.

## Requirements

- Python 3.x
- Operating system compatible with Python (Windows, Linux, macOS)

## Setup

1. Download the appropriate script (`a.py` or `a-full.py`).
2. Ensure Python 3.x is installed on your system.
3. Place the script in the directory you want to generate the file tree for.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script by executing `python a.py` or `python a-full.py`, depending on the version you choose.

## Examples

### a.py Output

```
project/
├── src/
│   ├── main.py
│   └── utils/
│       ├── helper.py
│       └── constants.py
└── README.md
```

### a-full.py Output

```
project/
├── 📁 src/
│   ├── 📄 main.py (Size: 1.23 KB, Last Modified: 2022-04-08 15:30:00)
│   └── 📁 utils/
│       ├── 📄 helper.py (Size: 0.75 KB, Last Modified: 2022-04-08 15:32:00)
│       └── 📄 constants.py (Size: 0.50 KB, Last Modified: 2022-04-08 15:35:00)
└── 📄 README.md (Size: 0.25 KB, Last Modified: 2022-04-08 15:40:00)
```

## Differences

- `a-full.py` provides advanced features such as icons, file sizes, last modified dates, and colorization, while `a.py` offers a basic file tree representation.
- The enhanced version enhances visual appeal and readability with colored output and additional file information.

Choose the script that best suits your needs based on the desired level of detail and visual presentation.

--- 

