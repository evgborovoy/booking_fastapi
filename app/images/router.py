from fastapi import UploadFile, APIRouter
import shutil

router = APIRouter(prefix="/images", tags=["Loading images"])

@router.post("/hotels")
async def add_image(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_obj:
        shutil.copyfileobj(file.file, file_obj)


