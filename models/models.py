from typing import Optional

from pynamodb.models import Model, StringAttribute, HashKey

class ItemModel(Model, meta_class=HashKey):
  id = StringAttribute(hash_key=True)
  data = StringAttribute()