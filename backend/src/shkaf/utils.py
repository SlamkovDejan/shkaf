import io
import os
from shutil import copyfileobj
from typing import BinaryIO

from fastapi import HTTPException
from PIL import Image
from pillow_heif import register_heif_opener
from rembg import remove

register_heif_opener()

IMAGES_FOLDER_PATH = "public/images"


def save_image(file: BinaryIO, image_name: str) -> str:
    image_dest_path = os.path.join(IMAGES_FOLDER_PATH, image_name)
    with open(image_dest_path, "wb") as buffer:
        copyfileobj(file, buffer)
    return image_dest_path.removeprefix("public/")


def remove_background_from_image(image_data: bytes) -> bytes:
    try:
        input_image = Image.open(io.BytesIO(image_data))
        output_image = remove(input_image)

        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        return output_buffer.getvalue()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")
