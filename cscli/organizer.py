from pathlib import Path
import shutil
from utils import logger

# Mapping of file extensions to folder names
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx", ".md"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".json", ".xml", ".sh", ".ts", ".tsx", ".jsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"]
}

def organize_files(target_dir: str):
    """
    Organizes files in a directory into subdirectories based on their file type.
    """
    path = Path(target_dir)
    if not path.is_dir():
        logger.error(f"Error: Directory '{target_dir}' does not exist or is not a directory.")
        return
        
    files = [f for f in path.iterdir() if f.is_file()]
    if not files:
        logger.warning(f"No files found in '{target_dir}' to organize.")
        return
        
    logger.info(f"Found {len(files)} files. Starting organization...")
    
    moved_count = 0
    for file_path in files:
        ext = file_path.suffix.lower()
        folder_name = "Others"
        
        # Find matching category
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                folder_name = category
                break
                
        # Create target directory
        target_folder = path / folder_name
        target_folder.mkdir(exist_ok=True)
        
        # Move file safely
        target_file = target_folder / file_path.name
        
        # Handle conflict if file already exists in target folder
        counter = 1
        while target_file.exists():
            target_file = target_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1
            
        try:
            shutil.move(str(file_path), str(target_file))
            logger.info(f"Moved: {file_path.name} -> {folder_name}/")
            moved_count += 1
        except Exception as e:
            logger.error(f"Failed to move {file_path.name}: {e}")
            
    logger.info(f"Organization completed. Moved {moved_count} files into categories.")
