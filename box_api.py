import dataclasses
from typing import List
import copy


@dataclasses.dataclass
class Item:
    id: str
    type: str  # folder, file, web_link
    name: str
    children: List['Item'] = None

    def to_json(self):
        import json
        return json.dumps(self, default=lambda x: x.__dict__)


def get_folder_information(client, folder_id: str):
    # https://developer.box.com/reference/get-folders-id/
    folder = client.folder(folder_id=folder_id).get()
    return Item(folder.id, folder.type, folder.name)


def get_child_items(client, folder: Item):
    # https://developer.box.com/reference/get-folders-id-items/
    items = client.folder(folder_id=folder.id).get_items()
    _items = list(items)

    child_items = [get_child_items(client, Item(item.id, item.type, item.name)) if item.type == 'folder'
                   else Item(item.id, item.type, item.name)
                   for item in _items]

    _folder = copy.deepcopy(folder)

    _folder.children = child_items
    return _folder


def update_file(client, file_id: str, update_info):
    # see: https://developer.box.com/reference/put-files-id/
    # ex: update_info = {'description': 'My file'}
    # ex: update_info = {'name': 'New file name'}
    updated_file = client.file(file_id).update_info(update_info)


if __name__ == '__main__':
    pass  # Do nothing
