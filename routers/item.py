from fastapi import APIRouter, Depends, Body

from ..services import create_item, get_item, update_item, delete_item

router = APIRouter(prefix="/api/items")


@router.post("/")
async def create_item_handler(item: dict = Body(...)):
    await create_item(item)
    return {"message": "Item created successfully"}


@router.get("/{item_id}")
async def get_item_handler(item_id: str):
    item = await get_item(item_id)
    if item:
        return item
    else:
        return {"message": "Item not found"}


@router.put("/{item_id}")
async def update_item_handler(item_id: str, item_data: dict = Body(...)):
    await update_item(item_id, item_data)
    return {"message": "Item updated successfully"}


@router.delete("/{item_id}")
async def delete_item_handler(item_id: str):
    await delete_item(item_id)
    return {"message": "Item deleted successfully"}
