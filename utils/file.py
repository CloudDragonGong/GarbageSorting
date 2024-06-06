import os
def check_file_in_folder(folder, file_name):
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    else:
        return False