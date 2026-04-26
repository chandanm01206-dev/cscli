# cscli (Developer Productivity CLI)

`cscli` is a production-quality command-line tool built to automate real-world developer tasks cleanly and efficiently.

## Features

1. **Bulk Rename**: Sequentially rename files in a directory with custom prefixes, collision handling, and dry-run support.
2. **Project Generator**: Scaffold new projects instantly with a standard directory structure and boilerplate files.
3. **File Organizer**: Automatically tidy up messy directories by moving files into designated folders based on their extension.

## Requirements
* Python 3.10+

## Installation
Clone or download the repository, navigate to the `cscli` directory, and you can run it directly:
```bash
python main.py --help
```

## Commands & Usage

### 1. Bulk Rename
Rename all files in a folder sequentially.
```bash
# Preview changes (Dry Run)
python main.py rename --path ./my_images --prefix img_ --dry-run

# Apply changes
python main.py rename --path ./my_images --prefix img_
```

### 2. Generate Project
Scaffold a new project structure.
```bash
# Generates a project named 'my_app' in the current directory
python main.py generate --name my_app

# Generates in a specific directory
python main.py generate --name my_app --path ./projects/
```

### 3. File Organizer
Sort files in a target directory into subfolders (Images, Videos, Code, etc.)
```bash
python main.py organize --path ./downloads
```
