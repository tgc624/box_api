from boxsdk import JWTAuth, Client
from box_api import get_child_items, get_folder_information


if __name__ == '__main__':
    # see: https://developer.box.com/guides/authentication/jwt/with-sdk/
    config = JWTAuth.from_settings_file('./config.json')
    client = Client(config)

    root_folder_id = '123456789'
    root_folder = get_folder_information(client, root_folder_id)
    root_folder = get_child_items(client, root_folder)
