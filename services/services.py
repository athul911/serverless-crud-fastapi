from typing import Optional

from pynamodb.exceptions import DoesNotExist

from models.models import ItemModel


async def create_item(body: dict) -> None:
    item = ItemModel(id=body['id'], data=body['data'])
    await item.save()


async def get_item(item_id: str) -> Optional[dict]:
    try:
        item = await ItemModel.get(id=item_id)
        return item.dict()
    except DoesNotExist:
        return None


async def update_item(item_id: str, data: dict) -> None:
    try:
        item = await ItemModel.get(id=item_id)
        for key, value in data.items():
            setattr(item, key, value)
        await item.save()
    except DoesNotExist:
        pass


async def delete_item(item_id: str) -> None:
    try:
        item = await ItemModel.get(id=item_id)
        await item.delete()
    except DoesNotExist:
        pass
