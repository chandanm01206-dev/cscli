import os
from pathlib import Path
from utils import logger

def bulk_rename(target_dir: str, prefix: str, dry_run: bool = False):
    """
    Renames files in a directory sequentially with a given prefix.
    Preserves file extensions.
    """
    path = Path(target_dir)
    if not path.is_dir():
        logger.error(f"Error: Directory '{target_dir}' does not exist or is not a directory.")
        return

    files = [f for f in path.iterdir() if f.is_file()]
    if not files:
        logger.warning(f"No files found in '{target_dir}' to rename.")
        return

    logger.info(f"Found {len(files)} files. Starting bulk rename with prefix '{prefix}'...")
    
    for index, file_path in enumerate(sorted(files), start=1):
        new_name = f"{prefix}{index:03d}{file_path.suffix}"
        new_path = path / new_name

        # Handle naming conflicts by appending an extra suffix if the target exists
        counter = 1
        while new_path.exists() and new_path != file_path:
            new_name = f"{prefix}{index:03d}_{counter}{file_path.suffix}"
            new_path = path / new_name
            counter += 1

        if dry_run:
            logger.info(f"[DRY-RUN] Would rename: {file_path.name} -> {new_name}")
        else:
            try:
                if new_path != file_path:
                    file_path.rename(new_path)
                    logger.info(f"Renamed: {file_path.name} -> {new_name}")
            except Exception as e:
                logger.error(f"Failed to rename {file_path.name}: {e}")

    logger.info("Bulk rename operation completed.")
