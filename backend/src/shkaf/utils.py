import os
from shutil import copyfileobj
from uuid import uuid4

from fastapi import UploadFile

IMAGES_FOLDER_PATH = "public/images"


def save_image(image_file: UploadFile) -> str:
    ext = os.path.splitext(image_file.filename or "")[1]
    image_filename = f"{uuid4()}{ext}"
    image_dest_path = os.path.join(IMAGES_FOLDER_PATH, image_filename)
    with open(image_dest_path, "wb") as buffer:
        copyfileobj(image_file.file, buffer)
    return image_dest_path.removeprefix("public/")
