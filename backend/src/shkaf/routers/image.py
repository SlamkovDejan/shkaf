import io
from typing import Annotated, Any

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from shkaf.utils import remove_background_from_image

router = APIRouter()


@router.post("/rembg")
async def remove_background(
    file: Annotated[UploadFile, File(description="Image to remove background from")],
) -> Any:
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File is not an image")

    try:
        image_data = await file.read()
        processed_data = remove_background_from_image(image_data)

        filename = file.filename or "image"
        output_filename = filename.rsplit(".", 1)[0] + "_no_bg.png"

        return StreamingResponse(
            io.BytesIO(processed_data),
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename={output_filename}"},
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing {file.filename}: {str(e)}")
