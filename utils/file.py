import os
import uuid


def check_file_in_folder(folder, file_name):
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return True
    else:
        return False


def generate_unique_file_name(original_filename= 'picture.png'):
    filename , file_extension = os.path.splitext(original_filename)
    uuid_str = str(uuid.uuid4())
    new_filename = f"{filename}_{uuid_str}{file_extension}"
    return new_filename
