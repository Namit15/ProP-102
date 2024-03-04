import os
import shutil

from_dir = "C:/Users/naina/Downloads"
to_dir = "C:/Users/naina/Downloads/test"
file_ext_list = ['.txt', '.doc', '.docx', '.pdf']

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    path1 = os.path.join(from_dir, file)
    file_name, file_ext = os.path.splitext(file)

    if file_ext in file_ext_list:
        if not os.path.exists(to_dir + '/Document_Files'):
            os.makedirs(to_dir + '/Document_Files')

        path3 = to_dir + '/Document_Files/' + file

        if os.path.exists(path3):
            print(f"Moving {file} to {path3}")
            shutil.move(path1, path3)
        else:
            print(f"Moving {file} to {path3}")
            shutil.move(path1, path3)
