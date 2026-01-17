"""
Topic: Modern Path Handling with pathlib
Concepts: Path objects, path operations, file discovery, cross-platform paths
Learning objectives:
    - Use pathlib for object-oriented path manipulation
    - Navigate directories and discover files
    - Perform common file operations

Author: Parham Alvani (parham.alvani@gmail.com)
"""

__author__ = "Parham Alvani"

import shutil
from pathlib import Path

# === Creating Paths ===
print("=== Creating Paths ===")

# Current directory
cwd = Path.cwd()
print(f"Current directory: {cwd}")

# Home directory
home = Path.home()
print(f"Home directory: {home}")

# Create path from string
config_path = Path("/etc/hosts")
print(f"Config path: {config_path}")

# Join paths with /
project_path = Path.home() / "projects" / "python101"
print(f"Project path: {project_path}")


# === Path Properties ===
print("\n=== Path Properties ===")

example_path = Path("/home/user/documents/report.pdf")
print(f"Full path: {example_path}")
print(f"Name: {example_path.name}")  # report.pdf
print(f"Stem: {example_path.stem}")  # report
print(f"Suffix: {example_path.suffix}")  # .pdf
print(f"Parent: {example_path.parent}")  # /home/user/documents
print(f"Parts: {example_path.parts}")  # ('/', 'home', 'user', ...)


# === Checking Path Status ===
print("\n=== Path Status ===")

current = Path(".")
print(f"Exists: {current.exists()}")
print(f"Is directory: {current.is_dir()}")
print(f"Is file: {current.is_file()}")
print(f"Absolute path: {current.absolute()}")


# === File Discovery ===
print("\n=== File Discovery ===")

# List directory contents
current_dir = Path(".")
print("Files in current directory:")
for item in current_dir.iterdir():
    icon = "📁" if item.is_dir() else "📄"
    print(f"  {icon} {item.name}")

# Glob patterns
print("\nPython files (glob):")
for py_file in Path(".").glob("*.py"):
    print(f"  {py_file.name}")

# Recursive glob
print("\nAll Python files (recursive):")
for py_file in Path(".").rglob("*.py"):
    print(f"  {py_file}")


# === File Operations ===
print("\n=== File Operations ===")

test_file = Path("test_pathlib.txt")

# Write text
test_file.write_text("Hello from pathlib!\nLine 2")
print(f"Wrote to {test_file}")

# Read text
content = test_file.read_text()
print(f"Content: {content!r}")

# Get file info
stat = test_file.stat()
print(f"Size: {stat.st_size} bytes")

# Rename/move
new_file = Path("renamed_test.txt")
test_file.rename(new_file)
print(f"Renamed to {new_file}")

# Delete
new_file.unlink()
print(f"Deleted {new_file}")


# === Working with Directories ===
print("\n=== Directory Operations ===")

test_dir = Path("test_directory")

# Create directory (parents=True creates parent dirs if needed)
test_dir.mkdir(exist_ok=True)
print(f"Created {test_dir}")

# Create nested structure
(test_dir / "subdir").mkdir(exist_ok=True)
(test_dir / "subdir" / "file.txt").write_text("nested content")

# Remove directory (must be empty or use shutil.rmtree)
shutil.rmtree(test_dir)
print(f"Removed {test_dir} and contents")


# === Expected Output ===
# === Creating Paths ===
# Current directory: /current/working/dir
# Home directory: /home/user
# ...
#
# === Path Properties ===
# Full path: /home/user/documents/report.pdf
# Name: report.pdf
# Stem: report
# Suffix: .pdf
# ...

# === Exercises ===
# 1. Write a function that finds all files larger than a given size
# 2. Create a file organizer that moves files into folders by extension
