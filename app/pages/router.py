from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.hotels.router import get_all_hotels

router = APIRouter(prefix="/pages", tags=["Pages"])

templates = Jinja2Templates("app/templates")


@router.get("/hotels")
async def get_hotels_page(request: Request, hotels=Depends(get_all_hotels)):
    return templates.TemplateResponse("hotels.html", context={"request": request, "hotels": hotels})
