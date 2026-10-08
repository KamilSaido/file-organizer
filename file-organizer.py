"""
File Organizer
Takes a folder and sorts all things into corresponding folders.
"""

from pathlib import Path
import shutil

print("FILE ORGANIZER")
print("-----------------------")

file_folders = {
    # Images
    ".img": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".bmp": "Images",
    
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    
    # Data & Spreadsheets
    ".csv": "Spreadsheets",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".json": "Data",
    ".xml": "Data",
    
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".flac": "Audio",
    
    # Video
    ".mp4": "Video",
    ".avi": "Video",
    ".mkv": "Video",
    ".mov": "Video",
    
    # Archives & Compressed Files
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    
    # Executables & Installers
    ".exe": "Applications",
    ".msi": "Applications",
    ".dmg": "Applications",
    ".apk": "Applications"
}

# Moves the files to a correct folder
def move_to_folder(file):
    suffix = file.suffix.lower() # Get file ending and turn it lowercase

    if suffix in file_folders: # Check if it is in this dictionary
        folder_name = file_folders[suffix] # Name of the correct folder
        shutil.move(file, folder_path / folder_name) # Move it there
        print(f"Moved {file.name} -> {folder_name}")
    else:
        print(f"Skipped {file.name} (unknown file type)") # Unknown files

# Get the folder
folder_path = Path("C:/Users/Uzivatel/Documents/Development/Projects/Python/file-organizer/stuff")

# Check if it exists
if folder_path.is_dir():
    print("Folder: " + folder_path.name)
else:
    print(folder_path.name + " does not exist.")

# Make folders inside of the main folder
folders = ["Images", "Documents", "Spreadsheets", "Data", "Audio", "Video", "Archives", "Applications"]

# Looping through folder list and creating them
for file_type in folders:
    target_location = folder_path / file_type
    target_location.mkdir(exist_ok=True) # If it exists do not make it

# Loops through the folder
for file in folder_path.iterdir(): 
    if file.is_file(): # Checks if it is a file and not a folder
        move_to_folder(file)

print("Finished! Your files are now organized.")