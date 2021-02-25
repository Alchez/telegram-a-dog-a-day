import requests
import os

from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest

NAME = "photo"
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
DOGGO_API_ENDPOINT = "https://api.thedogapi.com/v1/images/search"
DOGGO_API_KEY = os.getenv("DOGGO_API_KEY")


def get_another_doggo():
    # get random image url from https://api.thedogapi.com
    headers = {"Content-Type": "application/json", "x-api-key": DOGGO_API_KEY}
    r = requests.get(DOGGO_API_ENDPOINT, headers=headers)

    if r.ok:
        # get image data from randomized image
        images = r.json()
        image_url = images[0].get("url")
        image_data = requests.get(image_url)
        image_filename = "image.png"

        # write to a local file
        with open(image_filename, "wb") as f:
            f.write(image_data.content)

        set_profile_picture(image_filename)


def set_profile_picture(image_filename):
    # start client
    client = TelegramClient(NAME, API_ID, API_HASH)
    with client:
        file_obj = client.upload_file(image_filename)
        client(UploadProfilePhotoRequest(file=file_obj))


if __name__ == '__main__':
    get_another_doggo()
