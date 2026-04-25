import argparse
from rename import bulk_rename
from generator import generate_project
from organizer import organize_files

def main():
    parser = argparse.ArgumentParser(
        prog="cscli",
        description="cscli - A Developer Productivity CLI Tool for automating real-world tasks."
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")
    
    # 1. Rename Command
    parser_rename = subparsers.add_parser("rename", help="Bulk rename files in a directory")
    parser_rename.add_argument("--path", required=True, help="Target directory path")
    parser_rename.add_argument("--prefix", required=True, help="Prefix for the new file names")
    parser_rename.add_argument("--dry-run", action="store_true", help="Preview changes without applying them")
    
    # 2. Generate Command
    parser_generate = subparsers.add_parser("generate", help="Generate a project folder structure and boilerplate")
    parser_generate.add_argument("--name", required=True, help="Name of the project")
    parser_generate.add_argument("--path", default=".", help="Base path where project will be created (default: current dir)")
    
    # 3. Organize Command
    parser_organize = subparsers.add_parser("organize", help="Organize files in a directory by type")
    parser_organize.add_argument("--path", required=True, help="Target directory to organize")
    
    args = parser.parse_args()
    
    if args.command == "rename":
        bulk_rename(target_dir=args.path, prefix=args.prefix, dry_run=args.dry_run)
    elif args.command == "generate":
        generate_project(project_name=args.name, base_path=args.path)
    elif args.command == "organize":
        organize_files(target_dir=args.path)

if __name__ == "__main__":
    main()
