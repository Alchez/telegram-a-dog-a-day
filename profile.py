import requests
import os

from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest

NAME = "photo"
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
DOGGO_API_ENDPOINT = "https://dog.ceo/api/breeds/image/random"

# start client
client = TelegramClient(NAME, API_ID, API_HASH)
client.start()

# get random image url from https://dog.ceo/dog-api/
r = requests.get(DOGGO_API_ENDPOINT)

if r.ok:
    # get image data from randomized image
    image_url = r.json().get("message")
    image_data = requests.get(image_url)
    image_filename = "image.png"

    # write to a local file
    with open(image_filename, "wb") as f:
        f.write(image_data.content)

    # upload profile picture
    file_obj = client.upload_file(image_filename)
    result = client(UploadProfilePhotoRequest(file=file_obj))