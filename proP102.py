import os
import shutil

# Define source directory and destination directory paths
from_dir = "C:/Users/naina/Downloads"
to_dir = "C:/Users/naina/Downloads/test"

# Define list of file extensions to be moved
file_ext_list = ['.txt', '.doc', '.docx', '.pdf']

# Get list of files in the source directory
list_of_files = os.listdir(from_dir)
print(list_of_files)

# Loop through each file in the source directory
for file in list_of_files:
    # Build the complete path for the source file
    path1 = os.path.join(from_dir, file)

    # Extract the file name and extension
    file_name, file_ext = os.path.splitext(file)

    # Skip files without extensions (e.g., hidden files)
    if not file_ext:
        continue

    # Check if the file extension is in the list to move
    if file_ext in file_ext_list:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(to_dir + '/Document_Files'):
            os.makedirs(to_dir + '/Document_Files')

        # Build the complete path for the destination file
        path3 = to_dir + '/Document_Files/' + file

        # Check if the destination file already exists
        if os.path.exists(path3):
            print(f"Moving {file} to existing file: {path3}")
        else:
            print(f"Moving {file} to new file: {path3}")

        # Move the file from source to destination
        shutil.move(path1, path3)
