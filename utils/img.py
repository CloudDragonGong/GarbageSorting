import os
import random
import shutil
from PIL import Image
from io import BytesIO
def mutation(output_dir,output_filename):
    img = get_random_image_filename(output_dir)
    copy_file_to_directory(os.path.join(output_dir,img), "./imgs",output_filename)

def copy_file_to_directory(src, dst,output_filename):
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copyfile(src,os.path.join(dst,os.path.basename(output_filename)))

def get_random_image_filename(folder_path):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith(('jpg', 'jpeg', 'png'))]
    if not image_files:
        return None
    random_image = random.choice(image_files)
    return random_image


def compress_image(image_path, quality=70):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="JPEG", quality=quality)
    buffered.seek(0)
    return buffered