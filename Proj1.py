import os
import shutil
from pathlib import Path

def organize_files(folder_path):
    """
    Organize files in a folder by their extensions.

    Args:
        folder_path (str): The path to the folder to be organized.
    """
    # Scan the folder and get a list of all files
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Create a dictionary to store the files by extension
    files_by_extension = {}
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_extension = Path(file).suffix[1:]  # Remove the dot from the extension
        if file_extension not in files_by_extension:
            files_by_extension[file_extension] = []
        files_by_extension[file_extension].append(file_path)

    # Create folders for each extension and move files into them
    for extension, files in files_by_extension.items():
        extension_folder = os.path.join(folder_path, extension)
        os.makedirs(extension_folder, exist_ok=True)
        for file in files:
            shutil.move(file, extension_folder)
            print(f"Moved {os.path.basename(file)} to {extension_folder}")

def main():
    # Prompt the user to select a folder
    folder_path = input("Enter the path to the folder you want to organize: ")
    if not os.path.exists(folder_path):
        print("The folder does not exist.")
        return

    organize_files(folder_path)
    print("Files have been organized.")

if __name__ == "__main__":
    main()
    
5
