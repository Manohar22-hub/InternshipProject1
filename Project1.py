import os
import shutil
from pathlib import Path

def organize_files(folder_path):
  
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    
    files_by_extension = {}
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_extension = Path(file).suffix[1:]
        if file_extension not in files_by_extension:
            files_by_extension[file_extension] = []
        files_by_extension[file_extension].append(file_path)

    
    for extension, files in files_by_extension.items():
        extension_folder = os.path.join(folder_path, extension)
        os.makedirs(extension_folder, exist_ok=True)
        for file in files:
            shutil.move(file, extension_folder)
            print(f"Moved {os.path.basename(file)} to {extension_folder}")

def main():
    
    folder_path = input("Enter the path to the folder you want to organize: ")
    if not os.path.exists(folder_path):
        print("The folder does not exist.")
        return

    organize_files(folder_path)
    print("Files have been organized.")

if __name__ == "__main__":
    main()
    
